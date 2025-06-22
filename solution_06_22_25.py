class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        n = len(s)
        print(n)
        for i in range(0, n, k):
            if i + k <= n:
                ret.append(s[i:i+k])
            else:
                ret.append(s[i:] + fill * (k - (n - i)))
        
        return ret
