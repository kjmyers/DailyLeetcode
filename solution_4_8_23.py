"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return None
        seen = {}

        def dfs(oNode):
            if oNode.val in seen:
                return seen[oNode.val]
            
            newNode = Node(oNode.val)
            seen[oNode.val] = newNode
            for nNode in oNode.neighbors:
                newNode.neighbors.append( dfs(nNode) )
            
            return newNode



        return dfs(node)
