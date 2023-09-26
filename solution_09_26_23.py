class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        c = Counter(s)
        stack = []

        for l in s:
            if l not in seen:
                while stack and stack[-1] > l and c[stack[-1]] > 0:
                    seen.remove(stack.pop())
                stack.append(l)
                seen.add(l)
            c[l] -= 1
        
        return ''.join(stack)
        
