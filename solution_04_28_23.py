class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        self.visit = set()
        self.adj = defaultdict(list)

        def dfs(node):
            self.visit.add(node)
            for neighbor in self.adj[node]:
                if neighbor not in self.visit:
                    dfs(neighbor)

        def isSimilar(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
            return diff == 0 or diff == 2

        n = len(strs)
        for i in range(n):
            for j in range(i+1, n):
                if isSimilar(strs[i], strs[j]):
                    self.adj[i].append(j)
                    self.adj[j].append(i)
        
        count = 0

        for i in range(n):
            if i not in self.visit:
                dfs(i)
                count += 1
        

        return count
                    
