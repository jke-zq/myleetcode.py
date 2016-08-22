class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        for __ in range(n - 1):
            pre, count = None, 0
            tmp = ""
            for s in ans:
                if s != pre:
                    if count:
                        tmp += str(count) + pre
                    pre = s
                    count = 1
                else:
                    count += 1
            if count:
                tmp += str(count) + pre
            ans = tmp
        return ans
