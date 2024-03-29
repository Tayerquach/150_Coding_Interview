import unittest
from Solution import Solution

class TwoSum(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for nums, target, result in [([2,7,11,15], 9, [0, 1]),
                                     ([3,2,4], 6, [1,2]),
                                     ([3,4,5], 6, []),
                                     ([3,3], 6, [0, 1])]:
            self.assertEqual(s.twoSum(nums, target), result)

if __name__ == "__main__":
    unittest.main()