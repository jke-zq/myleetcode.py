class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        hlen, nlen = len(haystack), len(needle)
        for i in range(hlen - nlen + 1):
            j = 0
            while j < nlen:
                if haystack[i + j] == needle[j]:
                    j += 1
                else:
                    break
            if j == nlen:
                return i
        return -1