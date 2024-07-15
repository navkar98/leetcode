# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        total_nodes = set()
        child_nodes = set()
        nodes = {}

        for i in descriptions:
            total_nodes.add(i[0])
            total_nodes.add(i[1])
            child_nodes.add(i[1])

            if i[0] not in nodes:
                nodes[i[0]] = {'left': None, 'right': None}

            if i[2] == 1:
                nodes[i[0]]['left'] = i[1]
            else:
                nodes[i[0]]['right'] = i[1]

        
        parent = list(total_nodes - child_nodes)

        def createTree(node):
            if not node:
                return
                
            curr_node = TreeNode(node)

            if node not in nodes:
                return curr_node
            
            left = createTree(nodes[node]['left'])
            if left:
                curr_node.left = left

            right = createTree(nodes[node]['right'])
            if right:
                curr_node.right = right

            return curr_node

        return createTree(parent[0])
 

        

