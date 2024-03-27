class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        curProd = 1
        ret = 0
        l = 0

        for r in range(len(nums)):
            curProd *= nums[r]
            while curProd >= k:
                curProd //= nums[l]
                l += 1
            ret += r - l + 1
        
        return ret
