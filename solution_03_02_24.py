class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        ret = [0] * len(nums)
        index = right
        
        while(left <= right):
            
            if abs(nums[left]) > abs(nums[right]):
                ret[index] = nums[left]**2
                left += 1
            else:
                ret[index] = nums[right]**2
                right -= 1
            index -= 1
            
        return ret
