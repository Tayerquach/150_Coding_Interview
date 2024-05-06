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

class SameTree(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for p, q, result in [([1,2,3], [1,2,3], True),
                             ([1,2], [1,None,2], False),
                             ([1,2,1], [1,1,2], False)]:
            p_tree = build_tree(0, p)
            q_tree = build_tree(0, q)
            self.assertEqual(s.isSameTree(p_tree, q_tree), result)

if __name__ == "__main__":
    unittest.main()
              



