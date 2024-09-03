class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        chs = ""
        for l in s:
            chs += str(ord(l) - 96)
        
        for _ in range(k):
            total = 0
            for l in chs:
                total += int(l)
            chs = str(total)

        return total
