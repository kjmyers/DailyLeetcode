class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ret = 0
        for c in s:
            if c == '(':
                stack.append(c)
                ret = max(ret, len(stack))
            elif c == ')':
                stack.pop()
        
        return ret
