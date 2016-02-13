class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # ret = []
        # if not nums:
        #     return ret
        # start, end = None, None
        # for n in nums:
        #     ##not start: 0 and None
        #     if start == None:
        #         start = n
        #         end = n
        #     else:
        #         if end + 1 != n:
        #             if start < end:
        #                 ret.append((start, end))
        #             else:
        #                 ret.append((start,))
        #             start = n
        #             end = n
        #         else:
        #             end = n
        # if start < end:
        #     ret.append((start, end))
        # else:
        #     ret.append([start])
        # return map(lambda x: "->".join([str(i) for i in x]) if len(x) == 2  else str(x[0]), ret)
        #solution b
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ranges = []
        if not nums:
            return ranges
        start, end = nums[0], nums[0]
        for i in xrange(1, len(nums) + 1):
            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += "->" + str(end)
                ranges.append(interval)
                if i < len(nums):
                    start = end = nums[i]
        return ranges
        #solution c
        return [re.sub('->.*>', '->', '->'.join(`n` for _, n in g))
            for _, g in itertools.groupby(enumerate(nums), lambda (i, n): n-i)]
 #ps:
 #1.如果在循环中只检测一次初始化，那么最好将初始化放在循环前面；
 #2.如果循环到结尾也是循环体内的逻辑条件，那么最好在循环体内检测这个循环条件，
 ##这样就不用在循环体结束后再在循环体后面也一遍循环体的逻辑了。
 ##此时最好使用下表索引的方式，下标最好到len的大小，这样如果初始化的是最后一个，for循环也会执行的。
 