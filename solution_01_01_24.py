class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        si = 0
        gi = 0
        g.sort()
        s.sort()

        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                gi += 1
            si += 1
        
        return gi
