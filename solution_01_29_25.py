class DSU:
    def __init__(self, n):
        self.size = [1] * n
        self.rep = list(range(n))
    
    def find(self, node):
        if self.rep[node] == node:
            return node
        self.rep[node] = self.find(self.rep[node])
        return self.rep[node]
    
    def union(self, n1, n2):
        n1 = self.find(n1)
        n2 = self.find(n2)

        if n1 == n2:
            return False
        else:
            if self.size[n1] > self.size[n2]:
                self.rep[n2] = n1
                self.size[n1] += self.size[n2]
            else:
                self.rep[n1] = n2
                self.size[n2] += self.size[n1]
            return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        dsu = DSU(len(edges))
        for edge in edges:
            if not dsu.union(edge[0] - 1, edge[1] - 1):
                return edge
