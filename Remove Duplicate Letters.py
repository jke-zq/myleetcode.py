class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## tle
        # def dfs(start, left, visited, tmp, length, lens, s, ans):
        #     # print start, tmp
        #     if left == 0:
        #         return True
        #     if start == lens:
        #         return False
            
        #     for index in range(length):
        #         if visited[index]:
        #             continue
        #         for i in range(start, lens):
        #             if s[i] == ans[index]:
        #                 visited[index] = True
        #                 tmp.append(s[i])
        #                 if dfs(i + 1, left - 1, visited, tmp, length, lens, s, ans):
        #                     return True
        #                 tmp.pop()
        #                 visited[index] = False
        #     return False
    
        # letters = [0] * 26
        # for ss in s:
        #     letters[ord(ss) - ord('a')] += 1
        # ans = []
        # for le in range(26):
        #     if letters[le] >= 1:
        #         ans.append(chr(ord('a') + le))
        # if len(ans) == len(s):
        #     return s
        # ## dfs to search the ans in s
        # tmp = []
        # length = len(ans)
        # # print ans
        # visited = [False] * length
        # lens = len(s)
        # dfs(0, length, visited, tmp, length, lens, s, ans)
        # return "".join(tmp)
        
        ## key: we can pop the front one by order, but we need to know if there are remaining ones after. So, we need remaining array.
        remaining = collections.defaultdict(int)
        for ss in s:
            remaining[ss] += 1
        ans_stack, ans_set = [], set()
        for ss in s:
            if ss in ans_set:
                remaining[ss] -= 1
                continue
            while ans_stack and ans_stack[-1] > ss and remaining[ans_stack[-1]]:
                ans_set.remove(ans_stack.pop())
            ans_stack.append(ss)
            ans_set.add(ss)
            remaining[ss] -= 1
        return "".join(ans_stack)
        
        