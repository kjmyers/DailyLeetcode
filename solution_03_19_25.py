class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        def flip(ind):
            for i in range(3):
                if ind+i < n:
                    nums[ind+i] ^= 1
        
        ret = 0
        for i in range(n-2):
            if nums[i] == 0:
                flip(i)
                ret += 1
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return ret
