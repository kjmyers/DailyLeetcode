class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_t = {}
        t_s = {}
        
        for sc, tc in zip(s,t):
            
            if sc not in s_t and tc not in t_s:
                s_t[sc] = tc
                t_s[tc] = sc
            
            if s_t.get(sc) != tc or t_s.get(tc) != sc:
                return False
        
        return True
