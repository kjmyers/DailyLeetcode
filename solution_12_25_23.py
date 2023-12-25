class Solution:
    def numDecodings(self, s: str) -> int:
        
        seen = {}

        def solve(i):
            if i in seen:
                return seen[i]
            if i >= len(s):
                return 1
            
            ret = 0
            if s[i] != "0":
                ret += solve(i+1)
                if i+1 < len(s) and int(s[i:i+2]) < 27:
                    ret += solve(i+2)
            
            seen[i] = ret
            return ret
        
        return solve(0)
