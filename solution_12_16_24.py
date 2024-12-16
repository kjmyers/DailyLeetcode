class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = []
        for i, num in enumerate(nums):
            heappush(h, (num, i))
        for _ in range(k):
            curn, curi = heappop(h)
            heappush(h, (curn * multiplier, curi))
        
        for num, i in h:
            nums[i] = num
        
        return nums
