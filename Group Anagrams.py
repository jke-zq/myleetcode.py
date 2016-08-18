import collections
import itertools
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # kinds = collections.defaultdict(list)
        # for s in strs:
        #     kinds["".join(sorted(s))].append(s)
        # return kinds.values()
        return [list(g) for k, g in itertools.groupby(sorted(strs, key=sorted), sorted)]
