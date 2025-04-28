class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ret = 0
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]
            while l <= r and total * (r - l + 1) >= k:
                total -= nums[l]
                l += 1
            ret += r - l + 1
        
        return ret
