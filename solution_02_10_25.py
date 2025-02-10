class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if 97 <= ord(c) <= 122:
                stack.append(c)
            else:
                stack.pop()
        
        return "".join(stack)
