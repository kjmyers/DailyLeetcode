class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        med = nums[n//2]

        ret = 0
        for num in nums:
            ret += abs(num - med)
        
        return ret
