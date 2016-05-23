class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # if not nums1 or not nums2:
        #     return []
        # setVal = set()
        # for n in nums1:
        #     setVal.add(n)
        # ans = []
        # for n in nums2:
        #     if n in setVal:
        #         ans.append(n)
        #         setVal.remove(n)
        # return ans
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        ans = []
        i, j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                while i < len1 and nums1[i] == nums1[i - 1]:
                    i += 1
                j += 1
                while j < len2 and nums2[j] == nums2[j - 1]:
                    j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans