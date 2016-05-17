# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # def do(node):
        #     if not node:
        #         return None
        #     right = do(node.left)
        #     ret = do(node.right)
        #     if right:
        #         right.right = node.right
        #         node.right = node.left
        #         node.left = None
        #     return node if not ret and not right else ret or right
        
        # do(root)
        def getRight(node):
            if not node:
                return None
            while node.right:
                node = node.right
            return node
            
        p = root
        while p:
            right = getRight(p.left)
            if right:
                p.right, right.right = p.left, p.right
                # print p.val, right.val
                p.left = None
            p = p.right