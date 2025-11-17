class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dist = k
        for i in range(n):
            if nums[i] == 1:
                if dist < k:
                    return False
                dist = 0
            else:
                dist += 1
        
        return True
