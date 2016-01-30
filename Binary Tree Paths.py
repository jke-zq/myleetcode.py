# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def doFind(node, tmp, ret):
            if not node:
                return
            else:
                tmp.append(node.val)
                if not node.left and not node.right:
                    ret.append("->".join([str(k) for k in tmp]))
                doFind(node.left, tmp, ret)
                doFind(node.right, tmp, ret)
                tmp.pop()
        ret = []
        tmp = []
        doFind(root, tmp, ret)
        return ret