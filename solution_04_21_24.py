class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        
        visited = [False] * n
                
        def dfs(node):
            if node == destination:
                return True
            if not visited[node]:
                visited[node] = True
                for next in graph[node]:
                    if dfs(next):
                        return True
            return False
        
        return dfs(source)
