class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rwords = [x[::-1] for x in words]
        
        return " ".join(rwords)
