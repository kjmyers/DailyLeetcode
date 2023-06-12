class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        n = len(nums)
        i = 0
        ret = []

        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] + 1 == nums[i+1]:
                i += 1
            
            if start != nums[i]:
                ret.append(str(start) + "->" + str(nums[i]))
            else: 
                ret.append(str(nums[i]))
            
            i += 1
        
        return ret
