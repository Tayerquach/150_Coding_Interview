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

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        """
        dtype p: TreeNode
        dtype q: TreeNode
        rtype: bool
        """
        if not p and not q: #If p and q are Null
            return True

        elif not p and q: #If p is Null and q is not Null
            return False

        elif p and not q: #If p is not Null and q is Null
            return False
        
        elif p.val != q.val: 
            return False

        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

class Invert_Binary_Tree(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_case(self):
        s = Solution()
        for input, result, flag in [([4,2,7,1,3,6,9], [4,7,2,9,6,3,1], True),
                              ([2,1,3], [2,3,1], True),
                              ([], [], True)]:
            root = build_tree(0, input)
            invert_tree = s.invertTree(root)
            expected_result = build_tree(0, result)
            expected_flag = isSameTree(invert_tree, expected_result)
            self.assertEqual(expected_flag, flag)

if __name__ == "__main__":
    unittest.main()

