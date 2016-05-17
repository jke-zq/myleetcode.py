# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(instart, inend, poststart, postend, inorder, postorder):
            if instart > inend:
                return None
            node = TreeNode(postorder[postend])
            index = inorder.index(node.val)
            node.left = helper(instart, index - 1, poststart, poststart + index - instart - 1, inorder, postorder)
            node.right = helper(index + 1, inend, poststart + index - instart, postend - 1, inorder, postorder)
            return node
            
        inLen = len(inorder)
        postLen = len(postorder)
        return helper(0, inLen - 1, 0, postLen - 1, inorder, postorder)
        