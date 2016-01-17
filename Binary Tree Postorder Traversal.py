# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        stack = [root]
        tag = [0]
        cur = root
        while cur.left:
            stack.append(cur.left)
            cur = cur.left
            tag.append(0)
        while stack:
            tail = stack[-1]
            if tag[-1]:
                tag.pop()
                ans.append(tail.val)
                stack.pop()
            else:
                tag[-1] = 1
                if tail.right:
                    stack.append(tail.right)
                    tag.append(0)
                    tail = tail.right
                    while tail.left:
                        stack.append(tail.left)
                        tag.append(0)
                        tail = tail.left
        return ans
                        