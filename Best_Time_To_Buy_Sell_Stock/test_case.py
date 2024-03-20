import unittest
from Solution import Solution

class BestTimeForStock(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result in [([7,1,5,3,6,4], 5),
                              ([7,6,4,3,1], 0)]:
            self.assertEqual(s.maxProfit(input), result)

if __name__ == "__main__":
    unittest.main() 