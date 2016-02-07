class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.snums = []
        for r in matrix:
            rows = [0]
            for c in r:
                rows.append(rows[-1] + c)
            self.snums.append(rows)
                

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret = 0
        for r in range(row1, row2 + 1):
            ret += self.snums[r][col2 + 1] - self.snums[r][col1]
        return ret


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)