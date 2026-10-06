"""Behavior checks for the one approved archive publication, without deployment."""

import importlib.util
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("publication", ROOT / "scripts/publish-newsletter-002.py")
publication = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publication)


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for relative in (publication.STAGED_PATH, publication.INDEX_PATH, publication.NAV_PATH):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / relative).read_bytes())

    def tearDown(self):
        self.temp.cleanup()

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def due(self):
        return publication.publish(self.root, datetime(2026, 10, 19, 11, 17, tzinfo=timezone.utc))

    def test_before_date_and_next_year_do_not_mutate(self):
        before = self.snapshot()
        for now in (
            datetime(2026, 10, 6, 15, tzinfo=timezone.utc),
            datetime(2026, 10, 19, 3, 59, tzinfo=timezone.utc),
            datetime(2026, 10, 20, 4, tzinfo=timezone.utc),
            datetime(2027, 10, 19, 11, 17, tzinfo=timezone.utc),
        ):
            self.assertFalse(publication.publish(self.root, now)["due"])
            self.assertEqual(before, self.snapshot())

    def test_target_date_publishes_exact_copy_and_rerun_is_idempotent(self):
        before = self.snapshot()
        result = self.due()
        self.assertTrue(result["due"])
        self.assertEqual(set(result["paths"]), {"docs/newsletter/002.md", "docs/newsletter/index.md", "mkdocs.yml"})
        expected = publication.read_text(self.root / publication.STAGED_PATH).replace(publication.DRAFT_LINE, publication.PUBLISHED_LINE)
        self.assertEqual(expected, publication.read_text(self.root / publication.ISSUE_PATH))
        self.assertEqual(1, publication.read_text(self.root / publication.INDEX_PATH).count(publication.ARCHIVE_ROW))
        self.assertEqual(1, publication.read_text(self.root / publication.NAV_PATH).count(publication.NAV_ROW))
        self.assertEqual(before["scheduled-newsletters/002.md"], self.snapshot()["scheduled-newsletters/002.md"])
        published = self.snapshot()
        self.assertFalse(self.due()["changed"])
        self.assertEqual(published, self.snapshot())

    def test_conflicting_issue_fails_before_other_writes(self):
        (self.root / publication.ISSUE_PATH).write_text("An unrelated issue", encoding="utf-8")
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "conflicts"):
            self.due()
        self.assertEqual(before, self.snapshot())

    def test_conflicting_archive_or_nav_fails_before_any_write(self):
        for relative, text in (
            (publication.INDEX_PATH, "\n- [Other title](002.md)\n"),
            (publication.NAV_PATH, "\n  - Different: newsletter/002.md\n"),
        ):
            original = (self.root / relative).read_bytes()
            with self.subTest(path=str(relative)):
                with (self.root / relative).open("a", encoding="utf-8") as handle:
                    handle.write(text)
                before = self.snapshot()
                with self.assertRaisesRegex(ValueError, "conflicting"):
                    self.due()
                self.assertEqual(before, self.snapshot())
            (self.root / relative).write_bytes(original)

    def test_changed_approved_copy_fails_without_mutation(self):
        with (self.root / publication.STAGED_PATH).open("a", encoding="utf-8") as handle:
            handle.write("Unapproved addition\n")
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, "approved draft"):
            self.due()
        self.assertEqual(before, self.snapshot())


if __name__ == "__main__":
    unittest.main()
