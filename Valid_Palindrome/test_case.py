import unittest
from Solution import Solution

class ValidPalindrome(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result in [("A man, a plan, a canal: Panama", True),
                              ("race a car", False),
                              (" ", True)]:
            self.assertEqual(s.isPalindrome(input), result)

if __name__ == "__main__":
    unittest.main()