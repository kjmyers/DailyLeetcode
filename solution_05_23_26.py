class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated = False

        for i in range(1, len(nums)):
            if rotated and nums[i] > nums[0]:
                return False
            if nums[i] < nums[i-1]:
                if rotated or nums[i] > nums[0]:
                    return False
                else:
                    rotated = True
        
        return True
