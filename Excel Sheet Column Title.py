class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # ret = ""
        # while n:
        #     left = n % 26
        #     if left == 0:
        #         # n -= 1
        #         left = 26
        #     ret += chr(ord("A") + left - 1)
        #     n = (n - 1) / 26
        # return ret[::-1]
        ##solution B
        result, dvd = "", n
        
        while dvd:
            dvd -= 1
            result += chr(dvd % 26 + ord('A'))
            dvd /= 26
        # return result[::-1]
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = []
        while n > 0:
            n -= 1
            char = chr(n % 26 + ord('A'))
            ans.append(char)
            n /= 26
        return "".join(ans[::-1])