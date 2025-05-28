class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for a,b in edges1:
            g1[a].append(b)
            g1[b].append(a)
        for a,b in edges2:
            g2[a].append(b)
            g2[b].append(a)
        
        def dfs(node, g, steps, seen):
            if node in seen or steps < 0:
                return 0
            seen.add(node)
            ret = 1
            for nxt in g[node]:
                ret += dfs(nxt, g, steps-1, seen)
            return ret
        
        secondMax = 0
        for i in range(len(edges2)+1):
            secondMax = max(secondMax, dfs(i,g2,k-1, set()))
        
        ret = [0] * (len(edges1)+1)

        for i in range(len(edges1)+1):
            ret[i] = dfs(i,g1,k, set()) + secondMax
        
        return ret