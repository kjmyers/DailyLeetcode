class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        
        ret = 0
        
        for c in s:
            letters[c] = letters.get(c, 0) + 1
        
        for k, i in letters.items():
            ret += (i // 2) * 2
        if ret < len(s):
            ret += 1
        
        return ret
