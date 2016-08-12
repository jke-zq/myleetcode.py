class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # while num > 1:
        #     if num % 4 == 0:
        #         num /= 4
        #     else:
        #         return False
        # return num == 1
        if num == 1:
            return True
        if num == 0:
            return False
        if num % 4 == 0:
            return self.isPowerOfFour(num / 4)
        else:
            return False
