import unittest
from utils import dicts


class TestDicts(unittest.TestCase):

    def setUp(self):
        self.data = {"vcs": "mercurial"}

    def test_get_val(self):
        self.assertEqual(dicts.get_val(self.data, "vcs"), "mercurial")
        self.assertEqual(dicts.get_val(self.data, "vcs", "git"), "mercurial")
        self.assertEqual(dicts.get_val({}, "vcs", "git"), "git")
        self.assertEqual(dicts.get_val({}, "vcs", "bazaar"), "bazaar")
