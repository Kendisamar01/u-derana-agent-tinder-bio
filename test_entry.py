import unittest

from main import ENTRY, MAX_CHARS


class EntryTests(unittest.TestCase):
    def test_entry_is_string(self):
        self.assertIsInstance(ENTRY, str)

    def test_entry_within_limit(self):
        self.assertLessEqual(len(ENTRY), MAX_CHARS)

    def test_entry_has_no_line_breaks(self):
        self.assertFalse(
            any(char in ENTRY for char in ("\n", "\r", "\u2028", "\u2029"))
        )


if __name__ == "__main__":
    unittest.main()
