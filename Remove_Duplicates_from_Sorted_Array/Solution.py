class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        type nums: List[int]
        rtype: int
        """

        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1

            

