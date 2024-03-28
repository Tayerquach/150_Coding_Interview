import unittest
from Solution import Solution

class WordPattern(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        solver = Solution()
        for pattern, s, result in [("abba", "dog cat cat dog", True),
                                   ("abba", "dog cat cat fish", False),
                                   ("aaaa", "dog cat cat dog", False)]:
            self.assertEqual(solver.wordPattern(pattern, s), result)

if __name__ == "__main__":
    unittest.main()