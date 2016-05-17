class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(r, c, start, visited, lenw, rows, cols, board, word, DICS):
            if start == lenw:
                return True
            if r >= rows or r < 0 or c >= cols or c < 0:
                return False
            if visited[r][c] or board[r][c] != word[start]:
                return False
            visited[r][c] = True
            for dx, dy in DICS:
                nx, ny = r + dx, c + dy
                if dfs(nx, ny, start + 1, visited, lenw, rows, cols, board, word, DICS):
                    return True
                    
            visited[r][c] = False
            
        if not board or not board[0] or word is None:
            return False
        ROWS, COLS = len(board), len(board[0])
        LENW = len(word)
        visited = [[False] * COLS for __ in range(ROWS)]
        DICS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0, visited, LENW, ROWS, COLS, board, word, DICS):
                    return True
        return False