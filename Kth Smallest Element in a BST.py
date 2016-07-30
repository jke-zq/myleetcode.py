# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        cur = root
        while k:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if k == 1:
                return cur.val
            k -= 1
            cur = cur.right

#########################################
#### need to be done:
#### to simplify the codes.
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        cur = root
        while k:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if k == 1:
                    return cur.val
                k -= 1
                cur = cur.right
