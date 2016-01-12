
#Binary Indexed Tree, BIT
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = nums[:]
        for i in range(1, len(nums)):
            sums[i] += sums[i - 1]
        osums = sorted(set(sums))
        ret = 0
        fwt = FenwickTree(len(nums))
        for sumi in sums:
            left = bisect.bisect_left(osums, sumi - upper)
            right = bisect.bisect_right(osums, sumi - lower)
            ret += fwt.sum(right) - fwt.sum(left) + (lower <= sumi <= upper)
            fwt.add(bisect.bisect_right(osums, sumi), 1)
            
        return ret
        
class FenwickTree(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)
    def lowbit(self, x):
        return x & (-x)
    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += self.lowbit(x)
    def sum(self, x):
        ret = 0
        while x > 0:
            ret += self.sums[x]
            x -= self.lowbit(x)
        return ret

#divide and conquer
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def countAndMerge(sums, start, end, lower, upper):
            if start >= end:
                return 0
            mid = (start + end) / 2
            cnt = countAndMerge(sums, start, mid, lower, upper) + \
            countAndMerge(sums, mid + 1, end, lower, upper)
            left, r, right = mid + 1, mid + 1, mid + 1
            tmp = []
            for i in range(start, mid + 1):
                while left <= end and sums[left] - sums[i] < lower:
                    left += 1
                while right <= end and sums[right] - sums[i] <= upper:
                    right += 1
                cnt += right - left
                while r <= end and sums[r] < sums[i]:
                    tmp.append(sums[r])
                    r += 1
                tmp.append(sums[i])
            sums[start:start + len(tmp)] = tmp
            return cnt
            
        sums = nums[:]
        for i in range(1, len(nums)):
            sums[i] += sums[i - 1]
        sums.insert(0, 0)
        return countAndMerge(sums, 0, len(sums) - 1, lower, upper)

##binary search tree