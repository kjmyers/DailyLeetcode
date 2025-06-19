class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        ret = 1
        curMin = nums[0]
        for i in range(0,len(nums)):
            if nums[i] - curMin > k:
                ret += 1
                curMin = nums[i]
        
        return ret 
