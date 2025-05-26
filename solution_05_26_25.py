class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = defaultdict(list)

        indegree = [0]*n

        for edge in edges:
            adj[edge[0]].append(edge[1])
        
        count = [ [0]*26 for _ in range(n) ]

        visit = [False] * n
        inStack = [False] * n
        answer = 0

        def dfs(node):
            nonlocal adj
            nonlocal count
            nonlocal visit
            nonlocal inStack

            if inStack[node]:
                return float('inf')
            if visit[node]:
                return count[node][ord(colors[node]) - ord('a')]
            
            visit[node] = True
            inStack[node] = True

            if node in adj.keys():
                for neighbor in adj[node]:
                    if dfs(neighbor) == float('inf'):
                        return float('inf')
                    for i in range(26):
                        count[node][i] = max(count[node][i],count[neighbor][i])
            
            count[node][ord(colors[node]) - ord('a')] += 1
            inStack[node] = False
            return count[node][ord(colors[node]) - ord('a')]



        for i in range(n):
            answer = max(answer, dfs(i))

        if answer == float('inf'):
            return -1
        else:
            return answer
