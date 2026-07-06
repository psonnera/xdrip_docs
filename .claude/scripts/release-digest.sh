#!/usr/bin/env bash
# Build a filtered commit digest between two xDrip release tags (or from FROM_TAG to HEAD-of-tags),
# one section per release, for use when writing changelog.md entries.
#
# Usage: release-digest.sh <xdrip_repo_path> <from_tag_exclusive> [to_tag_inclusive]
#   - If to_tag is omitted, walks every tag newer than from_tag, in order, up to the newest tag.
#
# Output goes to stdout: "== TAG (date) ==" header followed by filtered commit subjects for
# the range (previous_tag..TAG]. Noise (Crowdin/translation/merge/version-bump commits) is dropped.

set -euo pipefail

REPO="$1"
FROM_TAG="$2"
TO_TAG="${3:-}"

cd "$REPO"
git fetch --tags --quiet || true

# All release tags (YYYY.MM.DD[b] pattern), sorted chronologically.
mapfile -t ALL_TAGS < <(git tag -l '20*.*.*' | sort -t. -k1,1n -k2,2n -k3,3 )

# Slice to (FROM_TAG, TO_TAG] inclusive of TO_TAG, exclusive of FROM_TAG.
START_IDX=-1
for i in "${!ALL_TAGS[@]}"; do
  if [[ "${ALL_TAGS[$i]}" == "$FROM_TAG" ]]; then
    START_IDX=$i
    break
  fi
done
if [[ $START_IDX -eq -1 ]]; then
  echo "ERROR: from_tag '$FROM_TAG' not found in repo tags" >&2
  exit 1
fi

PREV="$FROM_TAG"
for ((i = START_IDX + 1; i < ${#ALL_TAGS[@]}; i++)); do
  TAG="${ALL_TAGS[$i]}"
  DATE=$(git log -1 --format=%as "$TAG")
  echo "== $TAG ($DATE) =="
  git log --format="- %s" "$PREV".."$TAG" \
    | grep -Eiv '^- (Merge |Crowdin|New translations|Update.*translation|Bump version|version bump)' \
    || true
  echo ""
  PREV="$TAG"
  if [[ -n "$TO_TAG" && "$TAG" == "$TO_TAG" ]]; then
    break
  fi
done
