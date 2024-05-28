class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        dif = [0] * n
        for i in range(n):
            dif[i] = abs(ord(s[i]) - ord(t[i]))
        
        ret = 0
        l = 0
        cur = 0
        
        for r in range(n):
            cur += dif[r]
            while cur > maxCost:
                cur -= dif[l]
                l += 1
            
            ret = max(ret, r - l + 1)
                
        return ret
