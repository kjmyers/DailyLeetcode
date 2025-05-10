class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        zeros1 = 0
        for num in nums1:
            if num == 0:
                zeros1 += 1
                sum1 += 1
            else:
                sum1 += num
        sum2 = 0
        zeros2 = 0
        for num in nums2:
            if num == 0:
                zeros2 += 1
                sum2 += 1
            else:
                sum2 += num
        
        if (zeros1 == 0 and sum2 > sum1) or (zeros2 == 0 and sum1 > sum2):
            return -1
        return max(sum1,sum2)
