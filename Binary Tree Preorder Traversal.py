# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = [root.val]
        cur = root
        while cur.left:
            stack.append(cur.left)
            ans.append(cur.left.val)
            cur = cur.left
            
        while stack:
            tail = stack[-1]
            stack.pop()
            if tail.right:
                stack.append(tail.right)
                ans.append(tail.right.val)
                tail = tail.right
                while tail.left:
                    stack.append(tail.left)
                    ans.append(tail.left.val)
                    tail = tail.left
        return ans
        