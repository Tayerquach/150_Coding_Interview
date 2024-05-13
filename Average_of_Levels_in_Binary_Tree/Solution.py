from collections import deque 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode):
        """
        type root: TreeNode
        rtype: List[float]
        """
        queue = deque([root])
        averages = []
        
        while queue:
            level_sum = 0
            level_cnt = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_sum += node.val
                    level_cnt += 1
                    queue.append(node.left)
                    queue.append(node.right)
            if level_cnt:
                averages.append(level_sum / level_cnt)
        return averages
                



        