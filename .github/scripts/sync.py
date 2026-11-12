"""Archive every accepted LeetCode submission. Python standard library only."""

import json
import os
from pathlib import Path
import re
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, HTTPRedirectHandler

ROOT = Path(__file__).resolve().parents[2]
EXTENSIONS = {
    "python": "py", "python3": "py", "cpp": "cpp", "java": "java",
    "c": "c", "csharp": "cs", "javascript": "js", "typescript": "ts",
    "golang": "go", "rust": "rs", "kotlin": "kt", "swift": "swift",
    "ruby": "rb", "scala": "scala", "php": "php", "dart": "dart",
    "mysql": "sql", "mssql": "sql", "oraclesql": "sql", "postgresql": "sql",
    "bash": "sh", "racket": "rkt", "erlang": "erl", "elixir": "ex",
    "elisp": "el", "r": "r", "pythondata": "py", "pandas": "py",
}


class SyncError(Exception):
    pass


class NoRedirects(HTTPRedirectHandler):
    # Never forward authentication cookies to another host or a login redirect.
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Client:
    def __init__(self, session, csrf):
        self.headers = {
            "Cookie": f"LEETCODE_SESSION={session}; csrftoken={csrf}",
            "x-csrftoken": csrf,
            "Referer": "https://leetcode.com/",
            "Origin": "https://leetcode.com",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 LeetCodePersonalArchive/1.0",
        }
        self.opener = build_opener(NoRedirects())

    def request(self, path, payload=None):
        for attempt in range(5):
            time.sleep(2)
            req = Request("https://leetcode.com" + path, headers=self.headers,
                          data=json.dumps(payload).encode() if payload else None)
            try:
                with self.opener.open(req, timeout=45) as response:
                    data = json.load(response)
                if not isinstance(data, dict):
                    raise SyncError("LeetCode returned an unexpected response.")
                return data
            except HTTPError as error:
                if error.code == 429 or error.code >= 500:
                    if attempt < 4:
                        time.sleep(min(10 * 2 ** attempt, 60))
                        continue
                if error.code in (401, 403, 302):
                    raise SyncError("LeetCode denied access. Refresh the session and CSRF secrets; "
                                    "a hosted runner may also be blocked by LeetCode.") from None
                raise SyncError(f"LeetCode request failed (HTTP {error.code}).") from None
            except (URLError, TimeoutError):
                if attempt == 4:
                    raise SyncError("LeetCode could not be reached after five attempts.") from None
                time.sleep(10)
            except (ValueError, UnicodeError):
                raise SyncError("LeetCode returned non-JSON data, possibly a login or challenge page.") from None

    def graphql(self, query, variables=None):
        result = self.request("/graphql/", {"query": query, "variables": variables or {}})
        if result.get("errors") or not isinstance(result.get("data"), dict):
            raise SyncError("LeetCode GraphQL failed. The session or API schema may have changed.")
        return result["data"]

    def username(self):
        status = self.graphql("query { userStatus { isSignedIn username } }").get("userStatus")
        if not status or not status.get("isSignedIn") or not status.get("username"):
            raise SyncError("Not signed into LeetCode. Replace the session and CSRF secrets.")
        return status["username"]

    def page(self, offset):
        data = self.request(f"/api/submissions/?offset={offset}&limit=20")
        if not isinstance(data.get("submissions_dump"), list) or "has_next" not in data:
            raise SyncError("LeetCode submission history is unavailable; no progress was advanced.")
        return data["submissions_dump"], data["has_next"]

    def detail(self, submission_id):
        data = self.graphql("""query submissionDetails($submissionId: Int!) {
            submissionDetails(submissionId: $submissionId) {
                code statusCode question { titleSlug }
            }
        }""", {"submissionId": int(submission_id)}).get("submissionDetails")
        if not data or data.get("statusCode") != 10 or not isinstance(data.get("code"), str):
            raise SyncError(f"Accepted submission {submission_id} could not be downloaded.")
        return data


def collect(client):
    """Scan all pages, including rejected attempts; never rely on a recent-only feed."""
    accepted = {}
    offset = 0
    previous_page = None
    while True:
        rows, has_next = client.page(offset)
        ids = tuple(str(row["id"]) for row in rows)
        if has_next and (not rows or ids == previous_page):
            raise SyncError("LeetCode pagination stalled; refusing an incomplete history scan.")
        for row in rows:
            if row.get("status_display") == "Accepted":
                accepted[str(row["id"])] = row
        if not has_next:
            break
        offset += len(rows)
        previous_page = ids
    return sorted(accepted.values(), key=lambda row: (int(row["timestamp"]), int(row["id"])))


def save_state(root, state):
    path = root / ".github/sync-state.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def sync(client, root=ROOT, budget_seconds=2100):
    started = time.monotonic()
    state_path = root / ".github/sync-state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {
        "version": 1, "username": None, "submissions": {}, "next_index": {},
    }
    username = client.username()
    if state["username"] and state["username"] != username:
        raise SyncError("The session belongs to a different LeetCode account. Sync stopped.")
    state["username"] = username
    rows = collect(client)
    pending = [row for row in rows if str(row["id"]) not in state["submissions"]]
    imported = 0
    try:
        for row in pending:
            if time.monotonic() - started >= budget_seconds:
                print("Import checkpoint saved; remaining submissions will resume next run.")
                break
            submission_id = str(row["id"])
            detail = client.detail(submission_id)
            slug = detail["question"]["titleSlug"]
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
                raise SyncError("LeetCode returned an invalid problem slug.")
            language = row["lang"]
            if language not in EXTENSIONS:
                raise SyncError(f"Unsupported language {language!r}; add its extension mapping before retrying.")
            index = state["next_index"].get(slug, 0)
            destination = root / slug / f"submission-{index}.{EXTENSIONS[language]}"
            destination.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation protects existing code if state is lost or edited.
            with destination.open("x", encoding="utf-8", newline="") as output:
                output.write(detail["code"])
            state["submissions"][submission_id] = {
                "path": destination.relative_to(root).as_posix(),
                "timestamp": int(row["timestamp"]), "language": language,
            }
            state["next_index"][slug] = index + 1
            imported += 1
            save_state(root, state)
            print(f"Archived {slug}/submission-{index}.{EXTENSIONS[language]}", flush=True)
    finally:
        state["remaining"] = len(pending) - imported
        state["history_import_complete"] = state["remaining"] == 0
        save_state(root, state)
        message = (f"Imported {imported} accepted submissions. "
                   f"Archived total: {len(state['submissions'])}. Remaining: {state['remaining']}.")
        print(message)
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as summary:
                summary.write(message + "\n")
    return state


def main():
    session = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()
    if not session or not csrf:
        raise SyncError("Add LEETCODE_SESSION and LEETCODE_CSRF_TOKEN under repository Settings > "
                        "Secrets and variables > Actions, then run Daily LeetCode sync.")
    sync(Client(session, csrf))


if __name__ == "__main__":
    try:
        main()
    except (SyncError, OSError, KeyError, ValueError) as error:
        # Do not log response bodies, headers, environment variables, or cookies.
        print(f"::error::{error}", file=sys.stderr)
        sys.exit(1)
