class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(dict)
        for s, d, w in flights:
            g[s][d] = w
        pq = [(0,src, k+1)]
        vis = [0] * n
        
        while pq:
            w, node, step = heapq.heappop(pq)
            if node == dst:
                return w
            if vis[node] >= step:
                continue
            vis[node] = step
            for neighbor, dw in g[node].items():
                heapq.heappush(pq, (w+dw, neighbor, step-1))
        return -1
