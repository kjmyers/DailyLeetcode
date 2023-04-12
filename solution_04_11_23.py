class Solution:
    def removeStars(self, s: str) -> str:
        ret = []
        for i in range(len(s)):
            if s[i] == '*':
                ret.pop()
            else:
                ret.append(s[i])
        
        return ''.join(ret)
