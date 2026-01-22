class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        cur = nums
        ret = 0
        while cur != sorted(cur):
            ret += 1
            sums = [cur[i] + cur[i+1] for i in range(len(cur)-1)]
            ind = sums.index(min(sums))
            nex = cur[:ind] + [sums[ind]] + cur[ind+2:]
            cur = nex
        return ret
