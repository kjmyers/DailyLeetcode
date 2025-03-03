class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        equal = 0
        n = len(nums)
        front = 0
        back = n - 1
        ret = [pivot] * n

        for i in range(n):
            if nums[i] < pivot:
                ret[front] = nums[i]
                front += 1
            if nums[n-1-i] > pivot:
                ret[back] = nums[n-1-i]
                back -= 1
        
        return ret
