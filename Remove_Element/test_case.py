import unittest

from Solution import Solution

class RemoveElement(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result in [(([3,2,2,3], 3), 2),
                              (([0,1,2,2,3,0,4,2], 2), 5)]:
    
            self.assertEqual(s.removeElement(input[0], input[1]), result) 

if __name__ == "__main__":
    unittest.main()
