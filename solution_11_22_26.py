class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        first_b = 0
        while first_b < n and s[first_b] != 'b':
            first_b += 1
        
        last_a = n-1
        while last_a > -1 and s[last_a] != 'a':
            last_a -= 1
        
        return last_a < first_b
