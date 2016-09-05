import collections
import itertools
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_t = collections.defaultdict(int)
        for ss in t:
            hash_t[ss] += 1
        for ss in s:
            hash_t[ss] -= 1

        list_t = filter(lambda x:hash_t[x] > 0, hash_t.keys())
        return list_t[0]

