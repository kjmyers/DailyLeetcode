class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0


        def calcSubArrays(length):
            ret = 0
            for sub in range(length,0,-1):
                ret += (length - sub) + 1
            return ret

        
        i = 0
        ret = 0

        while i < n-1:
            if nums[i] == 0:
                j = i + 1
                while j < n and nums[j] == 0:
                    j += 1
                ret += calcSubArrays(j-i)
                i = j
            else:
                i += 1
        
        if nums[-2] != 0 and nums[-1] == 0:
            ret += 1
        
        return ret
