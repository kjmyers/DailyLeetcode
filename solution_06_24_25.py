class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ret = []
        highestCheckedIdx = 0
        n = len(nums)
        for checkKeyIdx in range(n):
            if nums[checkKeyIdx] == key:
                for i in range(max(checkKeyIdx - k, highestCheckedIdx), min(n, checkKeyIdx + k + 1)):
                    ret.append(i)
                highestCheckedIdx = checkKeyIdx + k + 1
        
        return ret
