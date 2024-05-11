import unittest
from Solution import Solution, TreeNode

def build_tree(index, values):
    if index < len(values) and values[index] is not None:
        node = TreeNode(values[index])
        node.left = build_tree(2 * index + 1, values)
        node.right = build_tree(2 * index + 2, values)
        return node
    return None

class PathSum(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_case(self):
        s = Solution()
        for values, targetSum, result in [([1,2,3], 5, False),
                                          ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22, True),
                                          ([], 0, False)]:
            root = build_tree(0, values)
            self.assertEqual(s.hasPathSum(root, targetSum), result)

if __name__ == "__main__":
    unittest.main()
            