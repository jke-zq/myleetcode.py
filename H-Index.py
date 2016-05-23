class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # if not citations:
        #     return 0
        # if max(citations) < 1:
        #     return 0
            
        # citations.sort()
        # length = len(citations)
        
        # for i in range(length):
        #     left = length - i
        #     if left <= citations[i]:
        #         return left
        
        ## hash talbe using array.
        if not citations:
            return 0
        length = len(citations)
        cnts = [0] * (length + 1)
        for c in citations:
            cnts[[c, length][c > length]] += 1
        sumV = 0
        for h in range(length, -1, -1):
            if sumV + cnts[h] >= h:
                return h
            sumV += cnts[h]
        return 0
        