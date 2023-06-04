class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def find(x):
            if self.parent[x] != x:
                self.parent[x] = find(self.parent[x])
            
            return self.parent[x]
        
        def union_set(x, y):
            xset = find(x)
            yset = find(y)

            if self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset
            elif self.rank[xset] > self.rank[yset]:
                self.parent[yset] = xset
            else:
                self.parent[yset] = xset
                self.rank[xset] += 1

        size = len(isConnected)
        self.parent = [0] * size
        self.rank = [0] * size
        self.count = size
        for i in range(size):
            self.parent[i] = i
        numComps = size

        for i in range(size):
            for j in range(i+1, size):
                if isConnected[i][j] and find(i) != find(j):
                    numComps -= 1
                    union_set(i,j)
        
        return numComps
