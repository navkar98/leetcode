# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def get_node_direction_string(node, req):
            if not node:
                return False

            if node.val == req:
                return True

            left = get_node_direction_string(node.left, req)
            right = get_node_direction_string(node.right, req)

            string = ''

            if type(left) is str:
                return 'L' + left
            elif left:
                return 'L'
            elif type(right) is str:
                return 'R' + right
            elif right:
                return 'R'
            else:
                return False

        source = get_node_direction_string(root, startValue)
        dest = get_node_direction_string(root, destValue)

        source = '' if type(source) is bool else source
        dest = '' if type(dest) is bool else dest

        n, m = len(source), len(dest)
        i = j = 0

        while i < n and j < m and source[i] == dest[j]:
            i += 1
            j += 1

        return (n-i)*'U' + dest[j:]