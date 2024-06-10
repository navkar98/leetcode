# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        if n <= 0:
            return
        
        node = TreeNode(preorder[0])
        node_index = inorder.index(preorder[0])
        left_count = len(inorder[:node_index])
        right_count = len(inorder[node_index+1:])

        node.left = self.buildTree(preorder[1:left_count+1], inorder[:left_count+1])
        node.right = self.buildTree(preorder[left_count + 1:], inorder[-right_count:])

        return node
        