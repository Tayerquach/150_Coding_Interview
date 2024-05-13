# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """
        type root: TreeNode
        rtype: int
        """
        if not root:
            return 0
        
        def depthLeft(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d
        
        def depthRight(node):
            d = 0
            while node:
                d += 1
                node = node.right
            return d
        
        left_depth = depthLeft(root)
        right_depth = depthRight(root)

        if left_depth == right_depth:
            return 2 ** left_depth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        