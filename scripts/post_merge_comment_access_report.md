# Post-merge comment access diagnostic

Merged PR: [#48 — check access](https://github.com/NoamBerkoLaor/openshift-virtualization-tests/pull/48).

## Supplied PR context

Counts describe items readable in this run, not total comments on GitHub.

| Source | Availability | Readable item count | Contains “Learnings added” as a heading or `<summary>`? |
| --- | --- | --- | --- |
| Top-level conversation / issue comments | Missing: original comment bodies were not supplied | 0 original comments; actual GitHub count unknown | Unknown; no original bodies to inspect |
| Inline review comments (Files changed), including thread replies | Missing | 0; actual GitHub count unknown | Unknown; no bodies to inspect |
| Pull request review bodies | Missing | 0; actual GitHub count unknown | Unknown; no bodies to inspect |
| Merged diff / PR summary / objectives | Available | 3 context items: 1 diff covering 1 file, 1 PR summary, 1 objectives block | No |

The objectives contain one comments-summary subsection describing four exchanges:
the author's parsing guidance, CodeRabbit's acknowledgment and learning, the
author's full-review request, and CodeRabbit's confirmation. This is a readable
summary, not four retrieved comments. It does not identify their original comment
types, provide complete bodies, or expose a “Learnings added” heading or summary
block. The PR description also includes a CodeRabbit release-notes summary; that
embedded text is not an independently supplied issue comment or review body.

The task states that the PR is merged; the objectives' statement that it is open
is historical supplied context. No live PR status was retrieved.

## GitHub MCP

- Availability: **Unavailable**. Inspection of the callable tool inventory found
  no GitHub MCP connection/tools and no tool-discovery interface for loading them.
- Exact connection name: unknown; no connection name is exposed.
- Issue-comment listing: could not be attempted because no GitHub MCP listing
  tool is callable. This is an availability failure, not a GitHub API response.
- Pull request review-comment listing, including thread replies: could not be
  attempted for the same reason.
- Issue comments retrieved: **0**; total on GitHub unknown.
- Review comments retrieved: **0**; total on GitHub unknown.
- Retrieved comments containing “Learnings added”: **0 retrieved matches**;
  whether any GitHub comment contains it remains unknown.

## Conclusion

Only supplied context can feed a learnings documenter in this run, using the
objectives' summarized parsing guidance with explicit summary-level attribution.
MCP cannot feed it because no GitHub MCP tools are available. Neither path exposes
original comment bodies or a verified “Learnings added” block, so exact comment
extraction cannot be established.
