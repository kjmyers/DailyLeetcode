class Solution:
    def processStr(self, s: str) -> str:
        cur = []

        for c in s:
            if c == "*":
                if cur:
                    cur.pop()
            elif c == "#":
                cur = cur + cur
            elif c == "%":
                cur = cur[::-1]
            else:
                cur.append(c)
        
        return "".join(cur)
