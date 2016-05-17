# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        ans = []
        cur = [root]
        while cur:
            nextLev = []
            for node in cur:
                if node.left:
                    nextLev.append(node.left)
                if node.right:
                    nextLev.append(node.right)
            ans.append(cur)
            cur = nextLev
        ans[1::2] = map(lambda x: x[::-1], ans[1::2])
        ans = map(lambda x: map(lambda y: y.val, x), ans)
        return ans