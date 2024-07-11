class Solution:
    def reverseParentheses(self, s: str) -> str:
        ret = ""
        stack = []

        for c in s:
            if c == ')':
                rev = []
                while stack[-1] != '(':
                    rev.append(stack.pop())
                stack.pop()
                stack += rev
            else:
                stack.append(c)
        
        return "".join(stack)
