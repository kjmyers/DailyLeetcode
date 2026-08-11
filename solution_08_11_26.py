class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1
        preSum = nums[0]
        n = len(nums)
        if n == 1:
            return nums[0] + 1
        while i < n and nums[i] == nums[i-1] + 1:
            preSum += nums[i]
            i += 1
        if preSum == nums[i-1]:
            preSum += 1
        c = set(nums[i:])
        while preSum in c:
            preSum += 1
        
        return preSum
