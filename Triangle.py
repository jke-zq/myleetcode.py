class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        ret = [0] * (len(triangle[-1]) + 1)
        for t in triangle:
            size = len(t)

            i = size
            ret[i] = ret[i - 1] + t[i - 1]
            for i in range(size - 1, 1, -1):
                ret[i] = min(ret[i], ret[i - 1]) + t[i - 1]
            if size > 1:
                i = 1
                ret[i] = ret[i] + t[i - 1]
            # ret[0] = ret[1]
            # for i in range(size, 0, -1):
            #     if i == size:
            #         ret[i] = ret[i - 1] + t[i - 1]
            #     else:
            #         ret[i] = min(ret[i], ret[i - 1]) + t[i - 1]
        
        return min(ret[1:])
                    
                    
                