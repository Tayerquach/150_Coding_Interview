import unittest
from Solution import Solution

class ValidParentheses(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        solver = Solution()
        for input, result in [("()", True),
                              ("()[]{}", True),
                              ("(]", False)]:
            self.assertEqual(solver.isValid(input), result)

if __name__ == "__main__":
    unittest.main()            