class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def doCount(left, right):
            if left >= right:
                return
            else:
                mid = (left + right) / 2
                doCount(left, mid)
                doCount(mid + 1, right)
                tmp = []
                j = mid + 1
                for i in range(left, mid + 1):
                    while j <= right and nums[index[i]] > nums[index[j]]:
                        tmp.append(index[j])
                        j += 1
                    tmp.append(index[i])
                    ret[index[i]] += j - (mid + 1)
                index[left:left + len(tmp)] = tmp
                #TLE
                # ##merge
                # right_left = mid + 1
                # for i in range(left, mid + 1):
                #     j = right_left
                #     while j <= right and nums[index[i]] > nums[index[j]]:
                #         ret[index[i]] += 1
                #         j += 1
                # ##sort
                # i, j = left, mid + 1
                # tmp = []
                # while i <= mid and j <= right:
                #     if nums[index[i]] > nums[index[j]]:
                #         tmp.append(index[j])
                #         j += 1
                #     else:
                #         tmp.append(index[i])
                #         i += 1
                # if j <= right:
                #     tmp.extend(index[j:right + 1])
                # if i <= mid:
                #     tmp.extend(index[i:mid + 1])
                # index[left:right + 1] = tmp
                        
                    
        n = len(nums)
        index = range(n)
        ret = [0] * n
        doCount(0, n - 1)
        return ret
##using  
#Divide and Conquer 
##Binary Indexed Tree 
##Segment Tree 
##Binary Search Tree

