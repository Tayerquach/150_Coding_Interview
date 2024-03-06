import unittest
from Solution import Solution

class MergedSortedArray(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case(self):
        s = Solution()
        for input, result in [(([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6]),
                          (([1], 1, [], 0), [1]),
                          (([0], 0, [1], 1), [1])]:
            self.assertEqual(s.merge(input[0], input[1], input[2], input[3]), result)
        

if __name__ == "__main__":
    unittest.main()
