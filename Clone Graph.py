# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        
        if not node:
            return None
        listNodes = [node]
        length = 1
        start = 0
        hashNodes = {}
        hashNodes[node] = UndirectedGraphNode(node.label)
        
        while start < length:
            cur = listNodes[start]
            start += 1
            # hashNodes[cur] = UndirectedGraphNode(cur.label)
            for nei in cur.neighbors:
                if nei not in hashNodes:
                    ## we need to update hashnodes when updating listnodes
                    hashNodes[nei] = UndirectedGraphNode(nei.label)
                    listNodes.append(nei)
                    length += 1
        
        for n in listNodes:
            for nei in n.neighbors:
                hashNodes[n].neighbors.append(hashNodes[nei])
        return hashNodes[node]
        # if node is None:
        #     return None
        # cloned_node = UndirectedGraphNode(node.label)
        # cloned, queue = {node:cloned_node}, [node]
        
        # while queue:
        #     current = queue.pop()
        #     for neighbor in current.neighbors:
        #         if neighbor not in cloned:
        #             queue.append(neighbor)
        #             cloned_neighbor = UndirectedGraphNode(neighbor.label)
        #             cloned[neighbor] = cloned_neighbor
        #         cloned[current].neighbors.append(cloned[neighbor])
        # return cloned[node]