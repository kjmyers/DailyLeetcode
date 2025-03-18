class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        longest = 1
        bits = 0

        for r in range(len(nums)):
            while bits & nums[r] != 0:
                bits ^= nums[l]
                l += 1
            
            bits |= nums[r]

            longest = max(longest, r - l + 1)
        
        return longest
