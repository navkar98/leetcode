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
        def createDict(node, cnt):
            if not node:
                return

            d[cnt] = node.val
            createDict(node.left, 2*cnt + 1)
            createDict(node.right, 2*cnt + 2)

        d = {}
        createDict(root, 0)
        return str(d)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        import ast
        data = ast.literal_eval(data)

        def decrypt(cnt):
            if cnt not in data:
                return

            node = TreeNode(data[cnt])
            node.left = decrypt(2*cnt + 1)
            node.right = decrypt(2*cnt + 2)

            return node

        return decrypt(0)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))