import unittest
from Solution import Solution, TreeNode

def build_tree(index, values):
    """
    It creates the left and right children by recursively calling build_tree with updated indices calculated as 2 * index + 1 for the left child and 2 * index + 2 for the right child. This index calculation is based on the properties of a binary tree stored in an array.
    """
    if index < len(values) and values[index] is not None:
        node = TreeNode(values[index])
        node.left = build_tree(2 * index + 1, values)
        node.right = build_tree(2 * index + 2, values)
        return node
    return None

class CountCompleteTreeNodes(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_case(self):
        s = Solution()
        for values, result in [([1,2,3,4,5,6], 6),
                               ([], 0),
                               ([1], 1)]:
            root = build_tree(0, values)
            self.assertEqual(s.countNodes(root), result)

if __name__ == "__main__":
    unittest.main()
