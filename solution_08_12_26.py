class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        f = defaultdict(int)
        ret = 0
        l = 0

        for r in range(len(nums)):
            f[nums[r]] += 1
            while f[nums[r]] > k:
                f[nums[l]] -= 1
                l += 1
            ret = max(r - l + 1, ret)
        
        return ret
