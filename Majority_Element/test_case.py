import unittest
from Solution import Solution

class MajorityElement(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result in [([3,2,3], 3), ([2,2,1,1,1,2,2], 2)]:
            self.assertEqual(s.majorityElement(input), result)

if __name__ == "__main__":
    unittest.main()
