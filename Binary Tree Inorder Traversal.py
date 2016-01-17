# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while root.left:
            stack.append(root.left)
            root = root.left
        while stack:
            node = stack[-1]
            ans.append(node.val)
            stack.pop()
            if node.right:
                stack.append(node.right)
                node = node.right
                while node.left:
                    stack.append(node.left)
                    node = node.left
        return ans