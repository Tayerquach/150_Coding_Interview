class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        """
        type nums: List[int]
        type k: int
        rtype: bool
        """
        hashset = {}
        for i, num in enumerate(nums):
            if num in hashset and abs(i - hashset[num]) <= k:
                return True
            hashset[num] = i
        return False