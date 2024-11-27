class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        def bfs(graph):
            q = deque([(0,0)])
            visited = set()

            while q:
                for _ in range(len(q)):
                    node, distance = q.popleft()
                    visited.add(node)
                    for nextNode in graph[node]:
                        if nextNode not in visited:
                            if nextNode == n-1:
                                return distance + 1
                            q.append((nextNode,distance+1))
        

        g = defaultdict(list)

        for i in range(n-1):
            g[i].append(i+1)
        
        ret = []
        for s,d in queries:
            g[s].append(d)
            ret.append(bfs(g))
            
        
        return ret
