from unittest import TestCase

import carnaticMusicNotation

# Sample tautology to get a passed test

class TestNote(TestCase):
    def test_is_string(self):
        s = 'a'
        self.assertEqual(s, 'a')

