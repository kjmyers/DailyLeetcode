class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        rightSum = sum(nums)
        leftSum = 0
        ret = 0
        for num in nums:
            if num == 0:
                if leftSum == rightSum:
                    ret += 2
                elif abs(leftSum - rightSum) == 1:
                    ret += 1
            else:
                leftSum += num
                rightSum -= num
        return ret
