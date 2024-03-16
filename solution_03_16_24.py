class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [-2] * (2*n + 1)
        arr[n] = -1

        maxlen = 0
        count = 0
        for i in range(n):
            count += -1 if nums[i] == 0 else 1
            if arr[count + n] >= -1:
                maxlen = max(maxlen, i - arr[count + n])
            else:
                arr[count + n] = i
        
        return maxlen
