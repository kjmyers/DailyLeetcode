class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            if num % 3:
                ret += 1
        
        return ret
