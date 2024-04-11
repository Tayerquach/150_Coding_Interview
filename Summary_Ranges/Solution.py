# Time Complexity : O(N)
# Space Complexity : O(1)
class Solution:
    def summaryRanges(self, nums):
        """
        type nums: List[int]
        rtype: List[str]
        """
        # Create a list of string to store the output result...
        output = []
        # Start traversing the array from idx = 0 till idx < sizeofarray in a while loop.
        idx = 0
        while idx < len(nums):
            # Mark the number at current index as beginning element of the range...
            beg = nums[idx]
            # Traverse the array beggining from current index & find the last element whose difference from previous element is exactly 1, i.e. nums[idx + 1] == nums[idx] + 1...
            while idx+1 < len(nums) and nums[idx+1] == nums[idx] + 1:
                idx += 1
            # Set this element as last element of the range...
            last = nums[idx]
            # If continuous element isn't present...
            if beg == last:
                output.append(str(beg))
            # If present...
            else:
                output.append(str(beg) + "->" + str(last))
            idx += 1
        return output      # Return the output result list...
