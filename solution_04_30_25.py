class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ret += 1
        
        return ret
