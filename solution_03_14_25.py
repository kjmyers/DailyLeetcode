class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 0
        r = max(candies)

        while l < r:
            m = (l + r + 1) // 2
            if self.allGetCandies(m, candies, k):
                l = m
            else:
                r = m - 1
        
        return l

    def allGetCandies(self, div, candies, k):
        total_piles = 0
        for cand in candies:
            total_piles += cand // div
        
        return total_piles >= k
