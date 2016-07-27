class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # def check(length, sets, valids):
        #     for i in range(length - 1):
        #         for j in range(i + 1, length):
        #             if docheck(i, j, sets):
        #                 valids[i][j] = True
        # def docheck(i, j, sets):
        #     if sets[i] & sets[j]:
        #         return True
        #     return False
            
        # if not words:
        #     return 0
        # length = len(words)
        # lens = [0] * length
        # sets = [None] * length
        # valids = [[False] * length for __ in range(length)]
        # words.sort()
        # # init lens
        # for i in range(length):
        #     # if words is None:
        #     lens[i] = len(words[i])
        #     sets[i] = set(words[i])
        # # init valids
        # check(length, sets, valids)

        # ans = 0
        # for i in range(length - 1):
        #     for j in range(i + 1, length):
        #         if valids[i][j]:
        #             ans = max(ans, lens[i] * lens[j])
        # return ans
        length = len(words)
        elements = [0] * length
        lens = [0] * length
        base = ord('a')
        for i in range(length):
            for s in words[i]:
                elements[i] |= 1 << (ord(s) - base)
            lens[i] = len(words[i])
            
        ans = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                if elements[i] & elements[j] == 0:
                    ans = max(ans, lens[i] * lens[j])
        return ans
            
            