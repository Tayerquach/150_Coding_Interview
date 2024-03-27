import unittest
from Solution import Solution

class IsomorphicStrings(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        solver = Solution()
        for s, t, result in [("egg", "add", True),
                             ("foo", "bar", False),
                             ("paper", "title", True)]:
            self.assertEqual(solver.isIsomorphic(s, t), result)

if __name__ == "__main__":
    unittest.main()            