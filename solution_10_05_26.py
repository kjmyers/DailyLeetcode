class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] #The score of the current frame

        for x in s:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                if v == 0:
                    stack.append(stack.pop() + 1)
                else:
                    stack.append(stack.pop() + 2 * v)

        return stack.pop()
