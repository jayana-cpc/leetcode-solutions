# LeetCode Solutions — @jayana-cpc

Accepted LeetCode submissions, archived automatically every day.

## Structure

Each problem has a folder at the repository root. Every accepted submission is
kept as a separate file containing the original code, without added headers.

```text
two-sum/
  submission-0.py
  submission-1.py
binary-search/
  submission-0.py
```

Submissions are numbered from zero per problem, oldest first during the initial
import. Distinct accepted attempts are preserved even when their code is identical.
Folder names use LeetCode's problem slugs. There are no topic or DSA parent folders.

## One-time setup

1. Sign into your LeetCode account in Safari.
2. Open Safari Settings > Advanced and enable the web developer features
   (called “Show Develop menu in menu bar” in older Safari versions).
3. On leetcode.com, open Develop > Show Web Inspector. In Storage > Cookies >
   https://leetcode.com, copy the values of `LEETCODE_SESSION` and `csrftoken`.
4. In this repository's Settings > Secrets and variables > Actions, add two
   repository secrets:

   | Secret name | Cookie value |
   | --- | --- |
   | `LEETCODE_SESSION` | `LEETCODE_SESSION` |
   | `LEETCODE_CSRF_TOKEN` | `csrftoken` |

5. Open Actions > Daily LeetCode sync > Run workflow, using branch `main`.

Do not put cookies in code, issues, commits, or chat. No personal GitHub token is
needed: the workflow uses GitHub's automatic repository token.

## Import and daily sync

The first run scans the full submission history available to your signed-in
account and imports every accepted submission it can retrieve. Later runs scan
the history again and download only submission IDs not already archived.

Large imports checkpoint after about 35 minutes; run the workflow again to
continue immediately, or let the next daily run continue. Successful downloads
are committed even if a later request fails. Check the run summary for the number
imported and remaining. A full import is only complete when remaining is zero.

The schedule is daily at 16:23 UTC (8:23 AM Pacific standard time / 9:23 AM Pacific
daylight time); GitHub may delay scheduled runs. You can also run it manually.
GitHub can disable schedules in public repositories after 60 days without activity.

If LeetCode expires the session, replace both secrets and rerun. LeetCode's
endpoints are unofficial and can change or block hosted runners; failures appear
in Actions rather than silently counting as a successful sync. The live import
must be verified after the secrets are configured.

Sync code, tests, and the submission-ID checkpoint live under `.github/` so the
root stays focused on solution folders. Keep `.github/sync-state.json`: it prevents
duplicate imports and preserves filenames. Never execute archived submissions in
the sync workflow.
