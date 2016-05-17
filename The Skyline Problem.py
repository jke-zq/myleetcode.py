import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        for b in buildings:
            points.append((b[0], -1 * b[2], 0))
            points.append((b[1], b[2], 1))
        points.sort()
        
        maxHeap = []
        ans = []
        for x, h, t in points:
            if t == 0:
                ## bad codes
                # if not maxHeap or maxHeap[0] > h:
                #     if maxHeap:
                #         ans[-1][1] = x
                #     ans.append([x, None, -1 * h])
                # heapq.heappush(maxHeap, h)
                if not maxHeap:
                    ans.append([x, None, -1 * h])
                elif maxHeap[0] > h:
                    ans[-1][1] = x
                    ans.append([x, None, -1 * h])
                heapq.heappush(maxHeap, h)
            else:
                ## bad codes
                # h = h * -1
                # maxHeap.remove(h)
                # heapq.heapify(maxHeap)
                # if not maxHeap or maxHeap[0] > h:
                #     ans[-1][1] = x
                #     if maxHeap:
                #         ans.append([x, None, -1 * maxHeap[0]])
                h = -1 * h
                maxHeap.remove(h)
                heapq.heapify(maxHeap)
                if not maxHeap:
                    ans[-1][1] = x
                elif maxHeap[0] > h:
                    ans[-1][1] = x
                    ans.append([x, None, -1 * maxHeap[0]])
                    
        return ans
            