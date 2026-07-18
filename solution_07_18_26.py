class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minN = min(nums)
        maxN = max(nums)
        return gcd(maxN, minN)
