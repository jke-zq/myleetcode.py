class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ##error:
        if n == 1:
            return [0]
        
        neigs = collections.defaultdict(set)
        for f, t in edges:
            neigs[f].add(t)
            neigs[t].add(f)
        
        pre_level, unvisited = [], set()
        for k in neigs.keys():
            if len(neigs[k]) == 1:
                pre_level.append(k)
            unvisited.add(k)
        while len(unvisited) > 2:
            cur_level = []
            for k in pre_level:
                unvisited.remove(k)
                for nei in neigs[k]:
                    neigs[nei].remove(k)
                    if len(neigs[nei]) == 1:
                        cur_level.append(nei)
            pre_level = cur_level
        return list(unvisited)