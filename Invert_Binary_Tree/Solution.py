# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        dtype root: TreeNode
        rtype: TreeNode
        """
        queue = [root]
        while len(queue) > 0:
            current_value = queue.pop(0)
            currentNode = TreeNode(current_value)

            if currentNode is not None:
                currentNode.left, currentNode.right = currentNode.right, currentNode.left
            queue.append(currentNode.left)
            queue.append(currentNode.right)
        return root