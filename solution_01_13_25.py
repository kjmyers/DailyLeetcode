class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)

        length = 0

        for v in c.values():
            if v % 2 == 1:
                length += 1
            else:
                length += 2
        
        return length
