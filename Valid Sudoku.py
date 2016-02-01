class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            rows = set()
            cols = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows:
                        return False
                    else:
                        rows.add(board[i][j])
                #cols
                if board[j][i] != '.':
                    if board[j][i] in cols:
                        return False
                    else:
                        cols.add(board[j][i])
        
        ##check nine 
        for n in range(9):
            values = set()
            for r in range((n / 3)  * 3, (n / 3) * 3 + 3):
                for c in range((n % 3) * 3, (n % 3) * 3 + 3):
                    if board[r][c] != '.':
                        if board[r][c] in values:
                            return False
                        else:
                            values.add(board[r][c])
        return True
                    
