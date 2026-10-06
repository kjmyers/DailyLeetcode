class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for l in s:
            if stack and l == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(l)
        
        return len(stack)
