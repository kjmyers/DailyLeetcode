class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for a,b in edges1:
            g1[a].append(b)
            g1[b].append(a)
        for a,b in edges2:
            g2[a].append(b)
            g2[b].append(a)
        
        def dfs(node, g, steps, even, seen):
            if node in seen:
                return
            seen.add(node)
            if not (steps % 2):
                even.add(node)
            for nxt in g[node]:
                dfs(nxt, g, steps+1, even, seen)
        
        even1 = set()
        even2 = set()
        m = len(edges1)+1
        n = len(edges2)+1

        dfs(0, g1, 0, even1, set())
        dfs(0, g2, 0, even2, set())
        maxSecond = max(len(even2), n - len(even2))
        ret = [0] * m

        for i in range(m):
            if i in even1:
                ret[i] = len(even1) + maxSecond
            else:
                ret[i] = m - len(even1) + maxSecond
            
        
        return ret
