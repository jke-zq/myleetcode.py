# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findPath(tmp, node, target):
            if not node:
                return
            else:
                tmp.append(node)
                if node == target:
                    return True
                if not findPath(tmp, node.left, target) and not findPath(tmp, node.right, target):
                    tmp.pop()
                    return False
                return True
        ppath, qpath = [], []
        findPath(ppath, root, p)
        findPath(qpath, root, q)
        for n in qpath[::-1]:
            if n in ppath:
                return n
        return None