class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h = []

        for num in nums:
            heappush(h, num)
        
        ret = 0
        while h[0] < k:
            x = heappop(h)
            y = heappop(h)
            heappush(h, min(x, y) * 2 + max(x, y) )
            ret += 1
        
        return ret
