class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        N = 0
        # Getting the true length
        for i, c in enumerate(s):
            if c.isdigit():
                N = N * int(c)
            else:
                N = N + 1
            if k <= N:
                break
        
        # Finding the letter
        for j in range(i, -1, -1):
            c = s[j]
            if c.isdigit():
                N /= int(c)
                k %= N
            else:
                if k == N or k == 0:
                    return c
                N -= 1
