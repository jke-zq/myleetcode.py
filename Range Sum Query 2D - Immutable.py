class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.sumMatrix = []
            return
        
        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        self.sumMatrix = [[0 for __ in range(cols)] for __ in range(rows)]
        for r in range(1, rows):
            for c in range(1, cols):
                self.sumMatrix[r][c] = self.sumMatrix[r - 1][c] + matrix[r - 1][c - 1]
        for r in range(1, rows):    
            for c in range(1, cols):
                self.sumMatrix[r][c] += self.sumMatrix[r][c - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.sumMatrix:
            return 0
        return (self.sumMatrix[row2 + 1][col2 + 1] + self.sumMatrix[row1][col1]
                  - self.sumMatrix[row2 + 1][col1] - self.sumMatrix[row1][col2 + 1])
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)