class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)

        for i in range(n):
            prod = gc = lc = nums[i]
            
            for j in range(i+1, n):
                prod = prod * nums[j]
                gc = gcd(gc, nums[j])
                lc = lcm(lc, nums[j])
                if prod > gc * lc:
                    break
                if prod == gc * lc:
                    ret = max(ret, j - i + 1)
        
        return ret
