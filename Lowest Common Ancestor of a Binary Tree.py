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
        # def findPath(tmp, node, target):
        #     if not node:
        #         return
        #     else:
        #         tmp.append(node)
        #         if node == target:
        #             return True
        #         if not findPath(tmp, node.left, target) and not findPath(tmp, node.right, target):
        #             tmp.pop()
        #             return False
        #         return True
        # ppath, qpath = [], []
        # findPath(ppath, root, p)
        # findPath(qpath, root, q)
        # for n in qpath[::-1]:
        #     if n in ppath:
        #         return n
        # return None
        ##note:the p and q node in the tree
        if not root:
            return None
        if root == p or root == q:
            return root
        ##Runtime Error
        # left, right = map(lambda x:self.lowestCommonAncestor(x, p, q), [root.left, root.right])
        left, right = [self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right)]
        return root if left and right else (left or right)