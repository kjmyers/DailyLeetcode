class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)

        ret = [-1] * n
        div = 2*k + 1

        if div > n:
            return ret

        total = sum(nums[:div])
        ret[k] = total // div

        for i in range(div, n):
            total = total - nums[i - div] + nums[i]
            ret[i - k] = total // div
        
        return ret
