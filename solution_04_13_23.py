class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        pushi = 0
        popi = 0

        n = len(pushed)

        while pushi < n and popi < n:
            if not stack: #empty stack
                stack.append(pushed[pushi])
                pushi += 1
            
            elif stack[-1] == popped[popi]:
                stack.pop()
                popi += 1
            
            else:
                stack.append(pushed[pushi])
                pushi += 1

        if popped[popi:][::-1] == stack:
            return True
        else:
            return False
