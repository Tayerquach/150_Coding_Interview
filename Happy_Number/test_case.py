import unittest
from Solution import Solution

class HappyNumber(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for n, result in [(19, True),
                          (2, False)]:
            self.assertEqual(s.isHappy(n), result)

if __name__ == "__main__":
    unittest.main()