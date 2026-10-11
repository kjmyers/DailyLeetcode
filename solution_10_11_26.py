class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)

        for i, num in enumerate(nums):
            if n % (i+1) == 0:
                ret += num*num
        
        return ret
