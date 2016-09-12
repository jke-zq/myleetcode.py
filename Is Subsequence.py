class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Memory Limit Exceeded
        def helper(s, t, s_start, t_start, s_len, t_len):
            if s_start == s_len:
                return True
            for i in range(t_start, t_len):
                if s[s_start] == t[i]:
                    if helper(s, t, s_start + 1, i + 1, s_len, t_len) is True:
                        return True
            return False

        ls, lt = len(s), len(t)
        return helper(s, t, 0, 0, ls, lt)

