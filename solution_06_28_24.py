class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)

        for r0,r1 in roads:
            g[r0].append(r1)
            g[r1].append(r0)
        
        h  = []
        for k,l in g.items():
            heappush(h, (-len(l), k))
        imp = [0] * n
        c = n
        while h:
            _ , val = heappop(h)
            imp[val] = c
            c -= 1
        ret = 0
        for r0,r1 in roads:
            ret += imp[r0] + imp[r1]
        
        return ret
