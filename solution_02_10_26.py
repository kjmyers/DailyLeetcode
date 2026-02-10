class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            seen = set()
            oddCnt = evenCnt = 0
            for j in range(i,n):
                if nums[j] not in seen:
                    seen.add(nums[j])

                    if nums[j] & 1:
                        oddCnt += 1
                    else:
                        evenCnt += 1
                
                if oddCnt == evenCnt:
                    res = max(res, j-i+1)

            if n - i <= res:
                return res
            
        return res
