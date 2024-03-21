import unittest
from Solution import Solution

class RomanToInterger(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result in [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994), ("D", 500)]:
            self.assertEqual(s.romanToInt(input), result)

if __name__ == "__main__":
    unittest.main()