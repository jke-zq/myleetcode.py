class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        cherry = 0
        ret = ""
        for i in range(max(len(a), len(b))):
            val = cherry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            val, cherry = val % 2, val / 2
            ret += str(val)
        
        if cherry:
            ret += "1"
        return ret[::-1]