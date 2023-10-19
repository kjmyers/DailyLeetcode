class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def check(x):
            stack = []
            for l in x:
                if l == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(l)
            return ''.join(stack)
        
        return check(s) == check(t)
