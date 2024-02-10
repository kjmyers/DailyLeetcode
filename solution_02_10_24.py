class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        def countAroundCenter(lo, hi):
            ans = 0
            while lo >= 0 and hi < n:
                if s[lo] != s[hi]:
                    break
                lo -= 1
                hi += 1
                ans += 1
            return ans
        
        ret = 0
        for i in range(n):
            ret += countAroundCenter(i,i)
            ret += countAroundCenter(i,i+1)
        return ret
