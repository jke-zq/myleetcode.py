class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.snums = []
        for n in nums:
            if self.snums:
                self.snums.append(self.snums[-1] + n)
            else:
                self.snums.append(n)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.snums[j] - (self.snums[i - 1] if i > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

###improve this code.