import unittest
from Solution import Solution, build_tree

class MaximumDepthOfBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for arr, result in [([3,9,20,None,None,15,7], 3),
                             ([1,None,2], 2)]:
            root = build_tree(0, arr)
            self.assertEqual(s.maxDepth(root), result)

if __name__ == "__main__":
    unittest.main()


