class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # more conditions
        # 1.sorted
        # 2.size compared
        # size of list
        # 1.one of them is larger than memory
        # 2.two of them are larger than memory
        nums1.sort()
        nums2.sort()
        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        ans = []
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return ans
