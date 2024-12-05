class Solution:
    def canChange(self, start: str, target: str) -> bool:

        if Counter(start) != Counter(target):
            return False
        
        n = len(start)
        ps,pt = 0,0

        while ps < n and pt < n:
            while ps < n and start[ps] == "_":
                ps += 1

            # skip underscores in target
            while pt < n and target[pt] == "_":
                pt += 1
            
            if ps == n or pt == n:
                return (ps == n and pt == n)
            
            if ((target[pt] != start[ps]) or
                (start[ps] == 'L' and ps < pt) or
                (start[ps] == 'R' and ps > pt)):
                return False
            pt += 1
            ps += 1
        
        return True
