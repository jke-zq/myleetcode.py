class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = 3
        dicts = collections.defaultdict(int)
        for n in nums:
            dicts[n] += 1
            # while len(dicts) == k:
            if len(dicts) == k:
                for x in dicts.keys():
                    dicts[x] -= 1
                    if dicts[x] == 0:
                        dicts.pop(x)
        dicts = dicts.fromkeys(dicts, 0)
        for n in nums:
            if n in dicts:
                dicts[n] += 1
        return filter(lambda x:dicts[x] > float(len(nums) / 3), dicts.keys())