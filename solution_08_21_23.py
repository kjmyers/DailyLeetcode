class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2,0,-1):
            if s.count(s[:i]) * i == n:
                return True
                
        
        return False
