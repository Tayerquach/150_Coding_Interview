import unittest
from Solution import Solution

class SummaryRanges(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result in [([0,1,2,4,5,7], ["0->2","4->5","7"]),
                              ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"])]:
            self.assertEqual(s.summaryRanges(input), result)

if __name__ == "__main__":
    unittest.main()