class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        ret = []
        row = [1]
        ret.append(row)
        for i in range(1, numRows):
            cur = [1]
            for r in range(len(row)):
                if r > 0:
                    cur.append(row[r] + row[r - 1])
            cur.append(1)
            ret.append(cur)
            row = cur
        return ret