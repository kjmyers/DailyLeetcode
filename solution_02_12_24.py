class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        ret = nums[0]
        retLen = 1
        intStart = 0

        for i in range(1,n):
            if nums[i] != nums[i-1] and i - intStart > retLen:
                ret = nums[i-1]
                retLen = i - intStart
                intStart = i
        
        if n - intStart > retLen:
            ret = nums[-1]

        return ret
