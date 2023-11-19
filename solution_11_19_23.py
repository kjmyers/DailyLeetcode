class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        add = 0
        ret = 0
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                add += 1
            ret += add


        return ret
