class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ret = 0
        for l in range(n):
            c = 0
            for r in range(l,n):
                if nums[r] == target:
                    c += 1
                else:
                    c -= 1
                if c > 0:
                    ret += 1
        
        return ret
