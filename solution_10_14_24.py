class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = []
        
        for num in nums:
            heappush(h,-num)
        
        ret = 0
        for _ in range(k):
            cur = heappop(h)
            ret += -cur
            heappush(h, -ceil(-cur/3))
        
        return ret
