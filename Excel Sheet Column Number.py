class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for c in s:
            ret = ret * 26 + ord(c) - ord('A') + 1
        return ret