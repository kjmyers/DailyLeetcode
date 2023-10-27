class Solution:
    def expand(self, s, left , right):
        L = left
        R = right
        
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1
    
    
    
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            length = max(len1, len2)
            
            if length > (end - start):
                start = i - (length - 1)//2
                end = i + length//2
        return s[start:(end+1)]
