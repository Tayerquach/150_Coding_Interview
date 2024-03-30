import unittest
from Solution import Solution

class ContainsDuplicateII(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for nums, k, result in [([1,2,3,1], 3, True),
                                ([1,0,1,1], 1, True),
                                ([1,2,3,1,2,3], 2, False)]:
            self.assertEqual(s.containsNearbyDuplicate(nums, k), result)
if __name__ == "__main__":
    unittest.main()