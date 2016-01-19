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