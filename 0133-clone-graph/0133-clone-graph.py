"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 

        visited = set()
        queue = [node]

        new_nodes = {}

        while queue:
            curr_node = queue.pop(0)

            if curr_node in visited:
                continue
            
            visited.add(curr_node)
            new_node = Node(curr_node.val)
            new_nodes[curr_node] = new_node

            for i in curr_node.neighbors:
                queue.append(i)

        visited = set()
        queue = [node]

        while queue:
            curr_node = queue.pop(0)

            if curr_node in visited:
                continue
            
            visited.add(curr_node)

            for i in curr_node.neighbors:
                queue.append(i)
                new_nodes[curr_node].neighbors.append(new_nodes[i])

        return new_nodes[node]