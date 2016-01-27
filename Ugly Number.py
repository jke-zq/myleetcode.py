class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # factors = [2, 3, 5]
        # for f in factors:
        #     while num:
        #         if num % f == 0:
        #             num /= f
        #         else:
        #             break
        # return num == 1
        
        if not num:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1