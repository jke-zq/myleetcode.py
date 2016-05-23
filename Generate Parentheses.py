class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, right, n, tmp, ans):
            if right == n:
                ans.append("".join(tmp))
            if left < n:
                tmp.append('(')
                dfs(left + 1, right, n, tmp, ans)
                tmp.pop()
            if left > right:
                tmp.append(')')
                dfs(left, right + 1, n, tmp, ans)
                tmp.pop()
                
        if n == 0:
            return []
        tmp, ans = [], []
        dfs(0, 0, n, tmp, ans)
        return ans