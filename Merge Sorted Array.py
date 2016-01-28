class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tail = m + n - 1
        m, n = m - 1, n - 1
        while n >= 0 and m >= 0:
            if nums2[n] > nums1[m]:
                nums1[tail] = nums2[n]
                n -= 1
            else:
                nums1[tail] = nums1[m]
                m -= 1
            tail -= 1
        
        if n >= 0:
            nums1[:n + 1] = nums2[:n + 1]
        
                