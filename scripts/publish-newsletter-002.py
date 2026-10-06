#!/usr/bin/env python3
"""Publish only the approved Prompt Academy #002 archive on October 19, 2026.

The workflow runs this before a strict build and commits only the three returned
paths. GitHub supplies the clock; there is deliberately no CLI date override.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


PUBLISH_DATE = date(2026, 10, 19)
TIMEZONE = ZoneInfo("America/New_York")
STAGED_PATH = Path("scheduled-newsletters/002.md")
ISSUE_PATH = Path("docs/newsletter/002.md")
INDEX_PATH = Path("docs/newsletter/index.md")
NAV_PATH = Path("mkdocs.yml")
APPROVED_SHA256 = "eaedb763678fd68e69bb6f31838ad023b5d9dff7ce172b2dcbf48f867890d11b"
DRAFT_LINE = "Issue #002 · DRAFT for review. Not published."
PUBLISHED_LINE = "Issue #002 · October 19, 2026"
ARCHIVE_ROW = "- [Issue #002: Give your agent a smaller job](002.md) · October 19, 2026"
NAV_ROW = "          - 'Issue #002: Give your agent a smaller job': newsletter/002.md"
NAV_ANCHOR = "          - 'Issue #001: Ask it twice': newsletter/001.md"


def read_text(path: Path) -> str:
    return path.read_bytes().decode("utf-8").replace("\r\n", "\n")


def publish(root: Path, now: datetime) -> dict:
    """Validate the complete change before writing; a rerun changes nothing."""
    if now.tzinfo is None:
        raise ValueError("The publication clock must include a timezone.")
    local_date = now.astimezone(TIMEZONE).date()
    if local_date != PUBLISH_DATE:
        return {"due": False, "changed": False, "paths": [], "local_date": str(local_date)}

    staged = read_text(root / STAGED_PATH)
    if hashlib.sha256(staged.encode("utf-8")).hexdigest() != APPROVED_SHA256:
        raise ValueError("The staged #002 copy differs from the approved draft.")
    if staged.count(DRAFT_LINE) != 1:
        raise ValueError("The staged #002 publication marker is missing or duplicated.")
    issue = staged.replace(DRAFT_LINE, PUBLISHED_LINE)
    issue_path = root / ISSUE_PATH
    if issue_path.exists() and read_text(issue_path) != issue:
        raise ValueError("Existing newsletter/002.md conflicts with approved #002.")

    index = read_text(root / INDEX_PATH)
    if "002.md" in index:
        if index.count("002.md") != 1 or ARCHIVE_ROW not in index.splitlines():
            raise ValueError("The archive already has a conflicting or duplicate #002 entry.")
        updated_index = index
    else:
        archive_anchor = "## The archive\n\n"
        if index.count(archive_anchor) != 1:
            raise ValueError("The expected newsletter archive heading changed.")
        updated_index = index.replace(archive_anchor, archive_anchor + ARCHIVE_ROW + "\n")

    nav = read_text(root / NAV_PATH)
    if "newsletter/002.md" in nav:
        if nav.count("newsletter/002.md") != 1 or NAV_ROW not in nav.splitlines():
            raise ValueError("Navigation already has a conflicting or duplicate #002 entry.")
        updated_nav = nav
    else:
        if nav.splitlines().count(NAV_ANCHOR) != 1:
            raise ValueError("The expected #001 navigation entry changed.")
        updated_nav = nav.replace(NAV_ANCHOR, NAV_ANCHOR + "\n" + NAV_ROW)

    proposed = [(ISSUE_PATH, issue), (INDEX_PATH, updated_index), (NAV_PATH, updated_nav)]
    changed_paths = []
    for relative, content in proposed:
        path = root / relative
        if path.exists() and read_text(path) == content:
            continue
        # Keep existing files' line endings so unrelated lines stay unchanged.
        newline = "\r\n" if path.exists() and b"\r\n" in path.read_bytes() else "\n"
        path.write_bytes(content.replace("\n", newline).encode("utf-8"))
        changed_paths.append(relative.as_posix())
    return {"due": True, "changed": bool(changed_paths), "paths": changed_paths, "local_date": str(local_date)}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    result = publish(root, datetime.now(TIMEZONE))
    print(json.dumps(result))
    if output := os.environ.get("GITHUB_OUTPUT"):
        with open(output, "a", encoding="utf-8") as handle:
            handle.write(f"due={str(result['due']).lower()}\n")
            handle.write(f"changed={str(result['changed']).lower()}\n")


if __name__ == "__main__":
    main()
