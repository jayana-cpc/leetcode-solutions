import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from io import BytesIO
from urllib.error import HTTPError

spec = importlib.util.spec_from_file_location("sync", Path(__file__).with_name("sync.py"))
archive = importlib.util.module_from_spec(spec)
spec.loader.exec_module(archive)


def row(number, status="Accepted", language="python3"):
    return {"id": number, "timestamp": str(number), "status_display": status, "lang": language}


class FakeClient:
    def __init__(self, rows, fail=None):
        self.rows, self.fail, self.downloaded = rows, fail, []

    def username(self):
        return "test-user"

    def page(self, offset):
        return self.rows[offset:offset + 2], offset + 2 < len(self.rows)

    def detail(self, number):
        if number == self.fail:
            raise archive.SyncError("Temporary failure")
        self.downloaded.append(number)
        return {"code": "# identical code\n", "statusCode": 10,
                "question": {"titleSlug": "two-sum"}}


class ArchiveTests(unittest.TestCase):
    def test_http_errors_distinguish_challenge_csrf_and_auth_without_body_leaks(self):
        cases = [
            (403, b"<title>Just a moment...</title> SECRET", "browser security challenge"),
            (403, b"CSRF verification failed SECRET", "rejected the CSRF check"),
            (401, b"SECRET", "Authentication was rejected"),
            (403, b"SECRET", "Access forbidden"),
        ]
        for status, body, expected in cases:
            with self.subTest(status=status, expected=expected):
                client = archive.Client("fake", "fake")
                error = HTTPError("https://leetcode.com/graphql/", status, "", {}, BytesIO(body))
                with patch.object(client.opener, "open", side_effect=error), patch.object(archive.time, "sleep"):
                    with self.assertRaises(archive.SyncError) as result:
                        client.request("/graphql/")
                self.assertIn(expected, str(result.exception))
                self.assertNotIn("SECRET", str(result.exception))

    def test_full_pagination_filters_rejected_and_keeps_identical_attempts(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            client = FakeClient([row(5), row(4, "Wrong Answer"), row(3), row(2), row(1)])
            state = archive.sync(client, root)
            self.assertEqual(client.downloaded, ["1", "2", "3", "5"])
            self.assertTrue(state["history_import_complete"])
            self.assertEqual(len(list((root / "two-sum").glob("*.py"))), 4)
            self.assertEqual((root / "two-sum/submission-0.py").read_text(), "# identical code\n")
            client.rows.insert(0, row(6, language="cpp"))
            client.downloaded.clear()
            archive.sync(client, root)
            self.assertEqual(client.downloaded, ["6"])
            self.assertTrue((root / "two-sum/submission-4.cpp").exists())

    def test_failure_checkpoints_and_rerun_resumes_without_duplicate(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            client = FakeClient([row(3), row(2), row(1)], fail="2")
            with self.assertRaises(archive.SyncError):
                archive.sync(client, root)
            state = json.loads((root / ".github/sync-state.json").read_text())
            self.assertEqual(set(state["submissions"]), {"1"})
            self.assertEqual(state["remaining"], 2)
            client.fail = None
            client.downloaded.clear()
            archive.sync(client, root)
            self.assertEqual(client.downloaded, ["2", "3"])

    def test_existing_file_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "two-sum").mkdir()
            path = root / "two-sum/submission-0.py"
            path.write_text("original")
            with self.assertRaises(FileExistsError):
                archive.sync(FakeClient([row(1)]), root)
            self.assertEqual(path.read_text(), "original")

    def test_expired_session_stops_before_history(self):
        client = archive.Client("fake", "fake")
        client.graphql = lambda *args: {"userStatus": {"isSignedIn": False}}
        with self.assertRaises(archive.SyncError):
            client.username()

    def test_time_budget_and_wrong_account(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            state = archive.sync(FakeClient([row(1)]), root, budget_seconds=0)
            self.assertFalse(state["history_import_complete"])
            self.assertEqual(state["remaining"], 1)
            client = FakeClient([row(1)])
            client.username = lambda: "another-user"
            with self.assertRaises(archive.SyncError):
                archive.sync(client, root)


if __name__ == "__main__":
    unittest.main()
