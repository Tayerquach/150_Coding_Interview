import unittest
from Solution import Solution, TreeNode

def build_tree(index, values):
    if index < len(values) and values[index] is not None:
        node = TreeNode(values[index])
        node.left = build_tree(2 * index + 1, values)
        node.right = build_tree(2 * index + 2, values)
        return node
    return None

class AverageOfLevelInBinaryTree(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_case(self):
        s = Solution()
        for values, result in [([3,9,20,None,None,15,7], [3.00000,14.50000,11.00000]),
                               ([3,9,20,15,7], [3.00000,14.50000,11.00000])]:
            root = build_tree(0, values)
            self.assertEqual(s.averageOfLevels(root), result)

if __name__ == "__main__":
    unittest.main()

