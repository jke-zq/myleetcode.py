class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        elems = collections.defaultdict(int)
        for c in s:
            elems[c] += 1
        for c in t:
            elems[c] -= 1
        return reduce(lambda x,y: x and y == 0, elems.values(), True)