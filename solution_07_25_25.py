class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        s = set()
        for num in nums:
            if num > 0:
                s.add(num)
        
        if len(s) == 0:
            return max(nums)
        
        ret = 0
        for n in s:
            ret += n
        
        return ret
