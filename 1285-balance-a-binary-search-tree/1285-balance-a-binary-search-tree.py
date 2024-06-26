# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedArray = []

        def getArr(node):
            if not node:
                return []
            
            left = getArr(node.left)
            sortedArray.append(node.val)
            right = getArr(node.right)
        
        
        def createBst(arr): 
            if not arr:
                return None
        
            mid = (len(arr)) // 2
        
            root = TreeNode(arr[mid])
            root.left = createBst(arr[:mid])
            root.right = createBst(arr[mid+1:])
            return root

        getArr(root)
        return createBst(sortedArray)