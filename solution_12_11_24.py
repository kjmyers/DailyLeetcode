class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        longest = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > 2*k:
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest
