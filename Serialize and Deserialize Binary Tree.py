# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        start = 0
        length = 1
        while start < length:
            node = queue[start]
            if node:
                queue.append(node.left)
                queue.append(node.right)
                length += 2
            start += 1
        while queue and queue[-1] == None:
            queue.pop()
        
        values = [str(node.val) if node else "#" for node in queue]
        return '|'.join(values)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        # print data
        data = data.split('|')
        length = len(data)
        queue = [TreeNode(int(data[0]))]
        start = 0
        index = 1
        while index < length:
            node = queue[start]
            start += 1
            leftV, rightV = data[index], data[index + 1] if index < length - 1 else "#"
            index += 2
            # print leftV, rightV
            if leftV != "#":
                node.left = TreeNode(int(leftV))
                queue.append(node.left)
            if rightV != "#":
                node.right = TreeNode(int(rightV))
                queue.append(node.right)
                
        return queue[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))