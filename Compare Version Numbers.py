class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        values1 = version1.split('.')
        values2 = version2.split('.')
        
        len1 = len(values1)
        len2 = len(values2)
        for i in range(max(len1, len2)):
            int1 = 0
            if i < len1:
                int1 = int(values1[i])
            int2 = 0
            if i < len2:
                int2 = int(values2[i])
            if int1 < int2:
                return -1
            elif int1 > int2:
                return 1
        return 0