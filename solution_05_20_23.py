class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        g = defaultdict(dict)
        for e, val in zip(equations, values):
            g[e[0]][e[1]] = val
            g[e[1]][e[0]] = 1.0/val
            
        def dfs(node, target, seen):
            if node not in g or target not in g:
                return -1.0
            
            if target in g[node]:
                return g[node][target]
            
            for i in g[node]:
                if i not in seen:
                    seen.add(i)
                    temp = dfs(i, target, seen)
                    if temp == -1:
                        continue
                    else:
                        return g[node][i] * temp
            return -1
        
        ret = []
        for q in queries:
            ret.append(dfs(q[0], q[1], set()))


        return ret
