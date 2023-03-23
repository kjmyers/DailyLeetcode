class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n-1:
            return -1

        graph = defaultdict(list)
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        
        seen = set()
        
        cables = -1

        def dfs(node):
            seen.add(node)
            for j in graph[node]:
                if j not in seen:
                    dfs(j)

        for i in range(n):
            if i not in seen:
                cables += 1
                dfs(i)
        
        return cables
        
Console
