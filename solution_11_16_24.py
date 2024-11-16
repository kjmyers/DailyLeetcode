class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ret = []
        for start in range(len(nums)-k+1):
            maxVal = -1
            for i in range(start+1,start+k):
                if nums[i] != (nums[i-1] + 1):
                    maxVal = -1
                    break
                maxVal = max(maxVal, nums[i])
            ret.append(maxVal)
        
        return ret
