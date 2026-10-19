class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ret = []
        for i in range(len(nums)):
            if nums[i] == target:
                ret.append(i)
        
        return ret
