# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        type root: TreeNode
        type targetSum: int
        rtype: bool
        """
        stack = [(root, targetSum)]
        while stack:
            node, curr_sum = stack.pop()
            if not node:
                continue
            elif not node.left and not node.right and curr_sum == node.val:
                return True
            stack.append((node.left, curr_sum - node.val))
            stack.append((node.right, curr_sum - node.val))
        return False