# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        points = []
        for inter in intervals:
            points.append((inter.start, 0))
            points.append((inter.end, 1))
        points.append((newInterval.start, 0))
        points.append((newInterval.end, 1))
        points.sort()
        ans = []
        count = 0
        for p, t in points:
            if t == 0:
                if count == 0:
                    inter = Interval(p, p)
                    ans.append(inter)
                count += 1
            else:
                count -= 1
                if count == 0:
                    ans[-1].end = p
        return ans