import unittest
from Solution import Solution

class LongestCommonPrefix(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result in [(["flower","flow","flight"], "fl"),
                              (["dog","racecar","car"], ""),
                              (["action", "actor", "a"], "a")]:
            self.assertEqual(s.longestCommonPrefix(input), result)

if __name__ == "__main__":
    unittest.main()