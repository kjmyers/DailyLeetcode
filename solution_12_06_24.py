class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banSet = set(banned)        
        total = 0
        ret = 0
        for i in range(1,n+1):
            if i not in banSet:
                total += i
                if total <= maxSum:
                    ret += 1

        return ret
