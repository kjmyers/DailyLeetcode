class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        for i in range(n):
            dist[i] /= speed[i]
        
        dist.sort()
        
        ret = 0
        for i in range(n):
            if dist[i] <= i:
                break
            ret += 1
        return ret
