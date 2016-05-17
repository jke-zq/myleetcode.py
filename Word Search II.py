class Solution(object):
    class TrieNode(object):
        def __init__(self):
            self.istring = False
            self.chars = {}
    class Trie(object):
        def __init__(self):
            self.root = Solution.TrieNode()
        def build(self, words):
            for w in words:
                p = self.root
                for c in w:
                    if c not in p.chars:
                        p.chars[c] = Solution.TrieNode()
                    p = p.chars[c]
                p.istring = True
                
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def dfs(r, c, node, visited, rows, cols, board, ans, tmp):
            if node.istring:
                ans.append("".join(tmp))
                # return
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c]:
                return

            if board[r][c] not in node.chars:
                return
            tmp.append(board[r][c])
            visited[r][c] = True
            nextNode = node.chars[board[r][c]]
            for dx, dy in DICTS:
                nr, nc = dx + r, dy + c
                dfs(nr, nc, nextNode,visited, rows, cols,  board, ans, tmp)
            visited[r][c] = False
            tmp.pop()
            
        if not board or not board[0] or not words:
            return []
        trie = Solution.Trie()
        trie.build(words)
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for __ in range(rows)]
        DICTS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ans = []
        tmp = []
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root, visited, rows, cols, board, ans, tmp)
        return list(set(ans))
        