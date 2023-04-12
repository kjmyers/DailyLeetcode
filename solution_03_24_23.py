class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(dict)

        for l,r in connections:
            graph[l][r] = 1
            graph[r][l] = -1
        
        #print(graph)

        ret = 0
        seen = set()

        def dfs(node):
            nonlocal ret
            seen.add(node)
            nextNodes = graph[node]
            for n, d in nextNodes.items():
                if n not in seen:
                    if d == 1:
                        #print(n)
                        ret += 1
                    dfs(n)
        
        dfs(0)
        return ret
