class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        if haystack == needle or needle == "":
            return 0
        hlen, nlen = len(haystack), len(needle)
        for i in range(hlen - nlen + 1):
            j = 0
            ret = i
            while ret < hlen and j < nlen:
                if haystack[ret] == needle[j]:
                    ret, j = ret + 1, j + 1
                else:
                    break
            if j == nlen:
                return i
        return -1