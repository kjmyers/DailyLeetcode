class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        nums.sort()
        if nums[-1] != nums[-2]:
            return False
        for i in range(len(nums)-1):
            if nums[i] != i+1:
                return False
        return True
