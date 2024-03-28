import unittest
from Solution import Solution

class ValidAnagram(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        solver = Solution()
        for s, t, result in [("anagram", "nagaram", True),
                             ("rat", "car", False)]:
            self.assertEqual(solver.isAnagram(s, t), result)

if __name__ == "__main__":
    unittest.main()            

                    