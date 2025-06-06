class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        stack = []
        ret = []
        minCharacter = "a"
        for c in s:
            stack.append(c)
            cnt[c] -= 1
            
            while minCharacter != "z" and cnt[minCharacter] == 0:
                minCharacter = chr(ord(minCharacter) + 1)
            while stack and stack[-1] <= minCharacter:
                ret.append(stack.pop())
        
        return "".join(ret)
