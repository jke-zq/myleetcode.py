class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        ## RE: MemoryError
        ## if k is bigger
        length = len(prices)
        if k >= length:
            local = prices[0]
            ret = 0
            for p in prices[1:]:
                if local < p:
                    ret += p - local
                    local = p
                else:
                    local = p
            return ret
        # local = [0] * (k + 1)
        # gl = [0] * (k + 1)
        local = [[0] * (k + 1) for __ in range(length)]
        gl = [[0] * (k + 1) for __ in range(length)]
        
        gl[0][0] = 0
        local[0][0] = 0
        # for i in range(1, k):
        #     local[0][i] = prices[0]
        #     gl[0][i] = prices[0]
        for i in range(1, length):
            # local[i][0] = 0
            # gl[i][0] = 0
            diff = prices[i] - prices[i - 1]
            # for j in range(k, 0, -1):
            for j in range(1, k + 1):
                # local[j] = max(gl[j - 1] + diff, local[j] + diff)
                # gl[j] = max(gl[j], local[j])
                local[i][j] = max(gl[i - 1][j - 1] + diff, local[i - 1][j] + diff)
                gl[i][j] = max(gl[i - 1][j], local[i][j])
        # return gl[k]
        return gl[length - 1][k]