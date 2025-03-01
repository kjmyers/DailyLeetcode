class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        ret = [0] * len(nums)
        cur = 0
        
        for i in range(len(nums)-1):
            if nums[i] != 0 and nums[i] == nums[i+1]:
                ret[cur] = nums[i] * 2
                nums[i+1] = 0
                cur += 1
            elif nums[i] > 0:
                ret[cur] = nums[i]
                cur += 1
        if nums[-1] > 0:
            ret[cur] = nums[-1]
        
        return ret
