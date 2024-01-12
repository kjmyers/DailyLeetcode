class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        s1 = s[:n]
        s2 = s[n:]
        print(s1, s2)

        vowels = set('aeiouAEIOU')
        c1 = 0
        c2 = 0

        for i in range(n):
            if s1[i] in vowels:
                c1 += 1
            if s2[i] in vowels:
                c2 += 1

        return c1 == c2
