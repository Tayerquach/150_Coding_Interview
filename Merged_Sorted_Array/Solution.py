class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        :type nums1: List[int]
        :type nums2: List[int]
        :type m: int
        :type n: int
        :rtype: List[int]
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

        return nums1


    