class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ret = []

        for c in s:
            if c == ")":
                stack.pop()
            if stack:
                ret.append(c)
            if c == "(":
                stack.append(c)
        
        return "".join(ret)
