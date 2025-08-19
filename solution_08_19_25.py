class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ret = 0
        numSub = 0

        for num in nums:
            if num == 0:
                numSub += 1
            else:
                numSub = 0
            ret += numSub
        
        return ret
