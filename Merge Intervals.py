# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        order_intervals = sorted(intervals, key = lambda x:x.start)
        index = 1
        while index < len(order_intervals):
            if order_intervals[index - 1].end < order_intervals[index].start:
                index += 1
            else:
                order_intervals[index - 1].end = max(order_intervals[index - 1].end, order_intervals[index].end)
                order_intervals.pop(index)
        return order_intervals



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
            
        lines = []
        for i in intervals:
            lines.append((i.start, 0))
            lines.append((i.end, 1))
        
        lines.sort()
        count = 0
        ans = []
        for p, t in lines:
            if t == 0:
                if count == 0:
                    ans.append([p, None])
                count += 1
            else:
                count -= 1
                if count == 0:
                    ans[-1][1] = p
        return ans
        