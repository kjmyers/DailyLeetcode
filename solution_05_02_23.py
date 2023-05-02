class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negs = 1

        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                negs *= -1
        
        return negs
