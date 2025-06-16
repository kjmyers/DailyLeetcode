class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ret = -1

        curmin = nums[0]

        for num in nums:
            if num <= curmin:
                curmin = num
            else:
                ret = max(ret, num - curmin)
        
        return ret
