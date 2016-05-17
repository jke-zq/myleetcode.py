class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(number):
            if number < 2:
                return False
            if number == 2:
                return True
            if number & 1 == 0:
                return False
            for i in range(3, int(number ** (0.5)) + 1, 2):
                if number % i == 0:
                    return False
            return True
            
        ans = 0
        for i in range(n):
            if check(i):
                ans += 1
        return ans

if __name__ == '__main__':
    print Solution().countPrimes(999983)