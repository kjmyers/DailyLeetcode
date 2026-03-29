class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True
        
        for i in range(2):
            set1 = set()
            set1.add(s1[i])
            set1.add(s1[i+2])

            set2 = set()
            set2.add(s2[i])
            set2.add(s2[i+2])
            if set1 != set2:
                return False
        
        return True
