import unittest
from Solution import Solution

class RemoveDuplicatesFromSortedArray(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result in [([1,1,2], 2),
                              ([0,0,1,1,1,2,2,3,3,4], 5)]:
            self.assertEqual(s.removeDuplicates(input), result)

if __name__ == "__main__":
    unittest.main()
    