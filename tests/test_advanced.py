# -*- coding: utf-8 -*-

from .context import sample

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())

    def test_sum(self):
        self.assertEqual(sample.simple_sum(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
