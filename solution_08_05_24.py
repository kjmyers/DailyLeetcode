class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s = set()
        
        count = defaultdict(int)
        for a in arr:
            count[a] += 1
        for key,v in count.items():
            if v == 1:
                s.add(key)
        
        c = 0
        for a in arr:
            if a in s:
                c += 1
                if c == k:
                    return a

        return ""
