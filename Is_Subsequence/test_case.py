import unittest
from Solution import Solution

class IsSubsequence(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        solver = Solution()
        for s, t, result in [("abc", "ahbgdc", True),
                             ("axc", "ahbgdc", False)]:
            self.assertEqual(solver.isSubsequence(s, t), result)

if __name__ == "__main__":
    unittest.main()