# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        # def do(node):
        #     if not node or (not node.left and not node.right):
        #         return
            
        #     other = node.next
        #     while other and (not other.left and not other.right):
        #         other = other.next
        #     # next = node.next.left or node.next.right
        #     nextq = None
        #     if other:
        #         nextq = other.left if other.left else other.right
        #     if not node.right:
        #         node.left.next = nextq
        #     elif not node.left:
        #         node.right.next = nextq
        #     else:
        #         node.left.next = node.right
        #         node.right.next = nextq
        #     do(node.right)
        #     do(node.left)
            
            
        # do(root)
        parent = root
        next, cur = None, None
        while parent:
            if not next:
                next = parent.left or parent.right
            if parent.left:
                if not cur:
                    cur = parent.left
                else:
                    cur.next = parent.left
                    cur = cur.next
            if parent.right:
                if not cur:
                    cur = parent.right
                else:
                    cur.next, cur = parent.right, parent.right
            parent = parent.next
            if not parent:
                parent = next
                next = None
                cur = None
                