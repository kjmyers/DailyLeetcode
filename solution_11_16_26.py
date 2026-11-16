class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            n = len(s)
            new_s = ""
            for group in range(0, n, k):
                cur = 0
                for i in range(min(k,n-group)):
                    cur += int(s[group+i])
                new_s += str(cur)
            s = new_s
        
        return s
