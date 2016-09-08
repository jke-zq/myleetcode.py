
import heapq


class Solution(object):

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        def find_by_col(matrix, k):
            m, n = len(matrix), len(matrix[0])
            vals = []
            for i in range(n):
                heapq.heappush(vals, (matrix[0][i], (0, i)))
            for __ in range(k - 1):
                __, (r, c) = heapq.heappop(vals)
                nextr = r + 1
                if nextr < m:
                    heapq.heappush(vals, (matrix[nextr][c], (nextr, c)))
            return heapq.heappop(vals)[0]

        def find_by_row(matrix, k):
            m, n = len(matrix), len(matrix[0])
            vals = []
            for i in range(m):
                heapq.heappush(vals, (matrix[i][0], (i, 0)))
            for __ in range(k - 1):
                __, (r, c) = heapq.heappop(vals)
                if c + 1 < n:
                    nextc = c + 1
                    heapq.heappush(vals, (matrix[r][nextc], (r, nextc)))
            return heapq.heappop(vals)[0]

        m, n = len(matrix), len(matrix[0])
        if m > n:
            return find_by_col(matrix, k)
        else:
            return find_by_row(matrix, k)
