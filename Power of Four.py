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
        ## solution two
        # if num == 1:
        #     return True
        # if num == 0:
        #     return False
        # if num % 4 == 0:
        #     return self.isPowerOfFour(num / 4)
        # else:
        #     return False

        ## solution tree
        # count0 = 0
        # count1 = 0
        # while num > 0:
        #     if (num & 1) == 1:
        #         count1 += 1
        #     else:
        #         count0 += 1
        #     num >>= 1
        # return count1 == 1 and (count0 % 2 == 0)
        n = num
        return n > 0 and (n & (n - 1) == 0) and (n & 0x55555555 != 0)
