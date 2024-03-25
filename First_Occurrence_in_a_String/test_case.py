import unittest
from Solution import Solution

class FirstOccurenceString(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for haystack, needle, result in [("sadbutsad", "sad", 0),
                              ("leetcode", "leeto", -1)]:
            self.assertEqual(s.strStr(haystack, needle), result)

if __name__ == "__main__":
    unittest.main()