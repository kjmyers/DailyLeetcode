class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)

        rtotal = sum(nums)
        ltotal = 0
        ret = 0
        for i in range(n-1):
            ltotal += nums[i]
            rtotal -= nums[i]
            if ltotal >= rtotal:
                ret += 1
        

        return ret
