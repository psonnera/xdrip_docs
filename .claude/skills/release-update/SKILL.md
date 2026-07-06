---
name: release-update
description: Bring xdrip_docs up to date after one or more new xDrip+ pre-releases. Mines commit history from the local xDrip source clone, updates changelog.md, then updates affected doc pages for new/changed/removed features. Use whenever the user says a new xDrip+ release/pre-release has shipped and docs need updating.
---

# xDrip+ release → docs update routine

Repeatable procedure for syncing this docs site after new upstream releases at
`https://github.com/NightscoutFoundation/xDrip`. Follow it end to end unless the user asks
for a narrower slice (e.g. "just the changelog").

## 0. Locate the local xDrip source clone

The docs repo does not vendor xDrip source. Find the user's local clone (has git remote
`upstream` = NightscoutFoundation/xDrip). If unsure of the path, ask, or check the previous
value recorded in project memory (`project_2025_2026_release_inventory.md` or its successor)
before searching the filesystem.

**Never read feature/behavior state from that clone's working tree.** It is normally checked
out on the user's personal dev branch (e.g. `OB1-G7`), not `master`. Any file content read
via a plain file read reflects that branch, not the release you're documenting. Always use:

```
git show <tag>:path/to/file
```

to inspect source as of a specific release tag. This applies to every verification step below.

## 1. Find the new tag(s) to document

1. Read the top row of `docs/changelog.md` — its tag is the last documented release.
2. In the local xDrip clone: `git fetch --tags`, then list tags newer than that one:
   `git tag -l '20*.*.*' | sort -t. -k1,1n -k2,2n -k3,3` and slice everything after the last
   documented tag.
3. If there are zero new tags, tell the user and stop — nothing to do.

## 2. Generate the commit digest (token-economic — do this instead of fetching GitHub release pages)

Run the helper script, which mirrors the approach used for the initial 80-release backfill:

```
bash .claude/scripts/release-digest.sh <xdrip_repo_path> <last_documented_tag>
```

Omit a `to_tag` to walk every new tag up to the newest. Output is one `== TAG (date) ==`
section per release with noise (Crowdin/translations/merges/version bumps) already filtered
out. Read this once instead of pulling release notes per-tag — GitHub release bodies for this
repo are just "Automated nightly build" and are not worth fetching.

## 3. Update `docs/changelog.md`

For each new tag, oldest-to-newest in the digest but inserted **newest-first** at the top of
the table (directly under the header row, above the current top row):

- Date format: `` [ 3rd Jul 2026](https://github.com/NightscoutFoundation/xDrip/releases/tag/2026.07.03) `` —
  note the leading space-padding for single-digit days to keep columns aligned, and ordinal
  suffixes (`1st`, `2nd`, `3rd`, `4th`...).
- `b`-suffix same-day releases: prefix the note with `b - `.
- Notes column: one short phrase per release summarizing the user-visible change from the
  digest. **Bold** the phrase (or the key term) for major features (new sensor/companion app,
  new follower capability, a feature the user will notice). Leave it terse/unbolded for
  internal fixes, and skip wording implying more detail than the commit subjects support.
- Do not link to doc pages that don't exist yet for a brand-new feature — those links get
  added in step 5 once the page itself is updated.

## 4. Build a feature inventory from the digest, and verify each claim before trusting it

Do not write documentation off a commit *title* alone — commit titles overstate or misdescribe
changes often enough to matter. For each digest entry that sounds user-facing, before touching
any doc page:

1. `git show <hash> --stat` in the xDrip clone to see which files changed.
2. `git show <hash> -- <file>` for the actual diff — prioritize `strings.xml` and
   `res/xml/pref_*.xml` / `xdrip_plus_prefs.xml`, since they show the exact label/summary text
   a user would see, or reveal that a change is purely an internal key rename with identical
   displayed text (this has happened twice already: "NovoPen improvements" and a Contour Next
   change were both internal-only).
3. Confirm the feature/setting still exists as of the newest tag with
   `git show <newest_tag>:<file>` — don't document something that was reverted later in the
   same batch of releases.

If a commit's purpose can't be determined from the message and diff alone (e.g. an internal
feature/class name with no descriptive commit body), do **not** invent documentation for it.
Add it to a "DEFERRED — needs investigation" list and **explicitly remind the user about it
in your final summary** — don't just leave it in memory silently. (Two prior examples of this:
NightLite, TxIdHelper — both still deferred as of 2026-07-06; check whether they've since been
resolved before re-flagging them.)

## 5. Update affected doc pages

Cross-reference each verified feature/removal against `docs/` (subfolders: `install/`, `use/`,
`calibrate/`, `smartwatch/`, `troubleshoot/`). For each page touched:

- Add new settings/features following the existing `!!!xdrip` / `!!!xdripitem` mockup
  conventions already used on that page — match the surrounding style exactly rather than
  introducing a new format.
- Remove documentation for retired features/devices — but only where the removal is confirmed
  in source (grep the page for the retired term, then confirm absence in the latest tag's
  source/prefs before deleting; some legacy mentions describe already-configured users and
  should stay, e.g. old sensors that "stop working" but not "never existed").
- Update the page's footer line to the newest tag covered:
  `` [*Last modified <d/m/yyyy>*](https://github.com/NightscoutFoundation/xDrip/releases/tag/<newest_tag>) ``.

## 6. Wrap up

- Leave all changes uncommitted — this repo's owner commits directly, don't commit for them
  unless asked.
- Report: which files changed, the key features added/removed, and read out the DEFERRED list
  from step 4 explicitly so it isn't missed.
- Update project memory (see `MEMORY.md` in the memory directory) with: the new "last
  documented tag", any newly deferred items, and any newly resolved ones from a prior pass.
