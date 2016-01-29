# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def doCheck(node, val, sum):
            if not node:
                return False
            val += node.val
            if not node.right and not node.left:
                return val == sum
            else:
                return doCheck(node.left, val, sum) or doCheck(node.right, val, sum)
        return doCheck(root, 0, sum)