# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    


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


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

