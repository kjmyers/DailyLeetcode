class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        l = 1
        ret = 0
        while l < len(nums) - 1:
            r = l+1
            while r < len(nums)-1 and nums[r] == nums[l]:
                r += 1
            
            if nums[l-1] > nums[l] and nums[r] > nums[l]:
                ret += 1
            if nums[l-1] < nums[l] and nums[r] < nums[l]:
                ret += 1
            
            l = r
        
        return ret
