class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
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

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        

        
