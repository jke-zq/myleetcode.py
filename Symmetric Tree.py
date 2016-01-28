# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ##Time Limit Exceeded
        # def check(nodes):
        #     left, right = 0, len(nodes) - 1
        #     while left < right:
        #         if nodes[left] and nodes[right] and nodes[left].val == nodes[right].val:
        #             left += 1
        #             right -= 1
        #         elif nodes[left] == nodes[right] == None:
        #             left, right = left + 1, right - 1
        #         else:
        #             return False
        #     return True
        # nodes = [root]
        # while nodes:
        #     allNone = reduce(lambda x, y: x and y == None, nodes, True)
        #     if allNone:
        #         return True
        #     else:
        #         symmetric = check(nodes)
        #         if not symmetric:
        #             return False
        #         else:
        #             next = []
        #             for n in nodes:
        #                 if n:
        #                     next.append(n.left)
        #                     next.append(n.right)
        #                 else:
        #                     next.append(None)
        #                     next.append(None)
        #             nodes = next
        # def doRecur(left, right):
        #     if not left and not right:
        #         return True
        #     if not left or not right or left.val != right.val:
        #         return False
        #     return doRecur(left.left, right.right) and doRecur(left.right, right.left)
        # if not root:
        #     return True
        # else:
        #     return doRecur(root.left, root.right)
        if not root:
            return True
        stack = [root.left, root.right]
        while stack:
            p, q = stack.pop(0), stack.pop(0)
            if not p and not q:
                continue
            elif not p or not q or p.val != q.val:
                return False
            else:
                stack.append(p.left)
                stack.append(q.right)
                stack.append(p.right)
                stack.append(q.left)
        return True
                