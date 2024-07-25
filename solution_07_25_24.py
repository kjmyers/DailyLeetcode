class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) < 2:
            return nums
        
        mid = len(nums)//2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        ret = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
        
        ret += left[i:]
        ret += right[j:]

        return ret
