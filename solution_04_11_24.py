class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []

        for d in num:
            while k > 0 and s and d < s[-1]:
                s.pop()
                k -= 1
            s.append(d)
        
        fs = s[:-k] if k else s

        return "".join(fs).lstrip('0') or "0"
