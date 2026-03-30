class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        even1 = defaultdict(int)
        even2 = defaultdict(int)
        odd1 = defaultdict(int)
        odd2 = defaultdict(int)
        for i in range(len(s1)):
            if i % 2:
                odd1[s1[i]] += 1
                odd2[s2[i]] += 1
            else:
                even1[s1[i]] += 1
                even2[s2[i]] += 1
        return even1 == even2 and odd1 == odd2
