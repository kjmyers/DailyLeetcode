class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums: List[int], k: int) -> int:
        ret = 0
        oddCount = 0
        left = 0
        for right in range(len(nums)):
            oddCount += nums[right] % 2
            while oddCount > k:
                oddCount -= nums[left] % 2
                left += 1
            
            ret += right - left + 1
        
        return ret
