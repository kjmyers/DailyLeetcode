class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        for cur in list(s):
            if stack and abs(ord(cur) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(cur)
        
        return "".join(stack)
