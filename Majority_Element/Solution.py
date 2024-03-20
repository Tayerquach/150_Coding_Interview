class Solution:
    def majorityElement(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        vote = 0
        majority = None

        for num in nums:
            if vote == 0:
                majority = num
            if num == majority:
                vote += 1
            else:
                vote -= 1
        return majority
        