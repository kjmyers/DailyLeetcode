class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        a = [ (y,x) for x,y in enumerate(nums) ]
        b = sorted(a)[(len(nums) - k):]
        c = [ (y,x) for x,y in b ]
        return [ x for _,x in sorted(c) ]
