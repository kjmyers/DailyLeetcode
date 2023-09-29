class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = -1 if nums[0] > nums[len(nums)-1] else 1
        
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1]) * direction < 0:
                return False

        return True
