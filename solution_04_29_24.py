class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = nums[0]
        for i in range(1,len(nums)):
            total ^= nums[i]
        
        ts = bin(total)
        ks = bin(k)
        ret = 0

        while k or total:
            if (k % 2) != (total % 2):
                ret += 1
            k //= 2
            total //= 2
        
        return ret
