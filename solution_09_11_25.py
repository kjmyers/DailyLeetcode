class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        cons = []
        left = 0
        right = 0
        V = {'A','E','I','O','U','a','e','i','o','u'}
        n = len(s)

        lastVowel = -1
        for i in range(n):
            if s[i] in V:
                if lastVowel+1 != i:
                    cons.append(s[lastVowel+1:i])
                lastVowel = i
                vowels.append(s[i])
                cons.append("")
        
        if lastVowel != n-1:
            cons.append(s[lastVowel+1:n])

        vowels.sort()
        
        cur = 0
        for i in range(len(cons)):
            if cons[i] == "":
                cons[i] = vowels[cur]
                cur += 1
        return "".join(cons)
