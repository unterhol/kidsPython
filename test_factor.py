#!/usr/local/bin/python3

import unittest
from factor import check_factorable


class TestFactor(unittest.TestCase):

    # run some tests against our check_factorable function to make sure
    # it works today, and doesn't get broken broken in the future if
    # the code gets changes.
    # run this with:  `python -m unittest discover`
    def test_factor(self):
        v1, v2 = check_factorable(5, 6)
        self.assertEqual(v1, 2)
        self.assertEqual(v2, 3)

        v1, v2 = check_factorable(-1, -6)
        self.assertEqual(v1, -3)
        self.assertEqual(v2, 2)

        v1, v2 = check_factorable(-7, 12)
        self.assertEqual(v1, -4)
        self.assertEqual(v2, -3)

        ans = check_factorable(-9, -22)
        self.assertEqual(ans[0], -11)
        self.assertEqual(ans[1], 2)

        ans = check_factorable(10, 1)
        self.assertIsNone(ans)


if __name__ == "__main__":
    unittest.main()
