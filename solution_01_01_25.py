class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        left = 1 if s[0] == "0" else 0
        right = 0
        for d in s[1:]:
            if d == "1":
                right += 1
        
        ret = left + right
        for i in range(1, n-1):
            if s[i] == "0":
                left += 1
            else:
                right -= 1
            ret = max(ret, left + right)

        return ret
