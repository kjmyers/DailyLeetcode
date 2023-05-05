class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        i = 0
        count = 0
        vowels = set(["a", "e", "i", "o", "u"])
        print(vowels)

        while i < k:
            if s[i] in vowels:
                count += 1
            i += 1
        
        n = len(s)
        ret = count
        while i < n:
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            ret = max(ret, count)
            i += 1
        
        return ret
