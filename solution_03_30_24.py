class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)
    
    def slidingWindowAtMost(self, nums: List[int], k: int) -> int:
        l = 0
        d = defaultdict(int)
        ret = 0
        for r in range(len(nums)):
            d[nums[r]] += 1
            
            while len(d) > k:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            
            ret += r - l + 1
        
        return ret
