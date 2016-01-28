# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def do(node):
            if not node:
                return 0
            left = do(node.left)
            if left < 0:
                return -1
            right = do(node.right)
            if right < 0:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return do(root) >= 0