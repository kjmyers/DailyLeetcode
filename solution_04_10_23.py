class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for l in s:
            if l in '])}':
                if not stack:
                    return False
                if l == ')' and stack[-1] != '(':
                    return False
                elif l == '}' and stack[-1] != '{':
                    return False
                elif l == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(l)
        
        if stack:
            return False
        else:
            return True
