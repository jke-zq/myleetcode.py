class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(r, c, visited, m, n, DICTS, grid):
            if r >= m or r < 0 or c >= n or c < 0:
                return 
            if visited[r][c] or grid[r][c] != "1":
                return
            visited[r][c] = True
            for dx, dy in DICTS:
                nx, ny = r + dx, c + dy
                dfs(nx, ny, visited, m, n, DICTS, grid)
            
            # visited[r][c] = False
            
            
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for __ in range(m)]
        DICTS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    dfs(i, j, visited, m, n, DICTS, grid)
        return count