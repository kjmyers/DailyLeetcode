class UnionFind:
    parent = []
    rank = []
    def __init__(self, size):
        self.parent = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.parent[i] = i
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if(xset == yset):
            return
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        for e in edges:
            dsu.union(e[0], e[1])
        
        compSize = defaultdict(int)
        for i in range(n):
            compSize[dsu.find(i)] += 1
        
        numPaths = 0
        remainNodes = n
        for key,item in compSize.items():
            c = item
            numPaths += c * (remainNodes - c)
            remainNodes -= c
        
        return numPaths
        
