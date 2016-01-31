class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        ret = [1]
        for i in range(rowIndex):
            pre, ret[0] = ret[0], 1
            for j in range(1, len(ret)):
                ret[j], pre = ret[j] + pre, ret[j]
            ret.append(1)
        return ret