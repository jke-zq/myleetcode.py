class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        twosum = collections.defaultdict(set)
        onums = sorted(nums)
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                twosum[onums[i] + onums[j]].add((i, j))
        
        ret = set()
        for i in range(size):
            for j in range(i + 1, size):
                left = target - onums[i] - onums[j]
                if left in twosum:
                    for i_i, i_j in twosum[left]:
                        if j < i_i:
                            ret.add((onums[i], onums[j], onums[i_i], onums[i_j]))
        
        return [list(k) for k in ret]