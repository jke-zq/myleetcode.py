# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        ## traverl
        # def traverl(node, leftMin, rightMax):
        #     if not node:
        #         return True
        #     if node.val <= leftMin or node.val >= rightMax:
        #         return False
        #     return traverl(node.left, leftMin, node.val) and traverl(node.right, node.val, rightMax)
        # if not root:
        #     return True
        # return traverl(root, float('-inf'), float('inf'))
        
        ## DC
        def dc(node):
            if not node:
                return True, float('inf'), float('-inf')
            leftRet = dc(node.left)
            rightRet = dc(node.right)
            if not leftRet[0] or not rightRet[0]:
                return False, 0, 0
            if leftRet[2] >= node.val:
                return False, 0, 0
            if rightRet[1] <= node.val:
                return False, 0, 0
            ret = True, min(leftRet[1], node.val), max(rightRet[2], node.val)
            return ret
        if not root:
            return True
        ans, __, __ = dc(root)
        return ans