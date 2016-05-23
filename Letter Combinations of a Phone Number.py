class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(start, tmp, ans, length, digits, lookups):
            if start == length:
                ans.append("".join(tmp))
                return
            index = int(digits[start])
            for i in lookups[index]:
                tmp.append(i)
                dfs(start + 1, tmp, ans, length, digits, lookups)
                tmp.pop()
                
        if not digits:
            return []
            
        lookups = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        tmp, ans = [], []
        length = len(digits)
        dfs(0, tmp, ans, length, digits, lookups)
        return ans