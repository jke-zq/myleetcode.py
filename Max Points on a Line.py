# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maxps = 0
        lens = len(points)
        for i in range(lens):
            start = points[i]
            ratios = collections.defaultdict(int)
            same = 1
            for j in range(i + 1, lens):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    same += 1
                else:
                    r = float("inf")
                    if start.x != end.x:
                        r = (start.y - end.y) * 1.0 / (start.x - end.x)
                    # ratios[r] = ratios.get(r, 0) + 1
                    ratios[r] += 1
            # cur_maxps = max(ratios.values()) + same if ratios else same
            cur_maxps = (max(ratios.values()) if ratios else 0) + same
            maxps= max(maxps, cur_maxps)
        return maxps
                    
        
        