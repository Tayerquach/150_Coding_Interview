import unittest
from Solution import Solution

class RansomNote(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for ransomNote, magazine, result in [("a", "b", False),
                                            ("aa", "ab", False),
                                            ("aa", "aab", True),
                                            ("aab", "baa", True)]:
            self.assertEqual(s.canConstruct(ransomNote, magazine), result)
        
if __name__ == "__main__":
    unittest.main()