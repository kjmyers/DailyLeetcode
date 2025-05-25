class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        c = Counter(words)
        center = 0
        ret = 0
        for word in words:
            reverse = word[1] + word[0]
            if reverse in c:
                if word[0] == word[1]:
                    numTake = (c[word] // 2) * 2
                    c[word] -= numTake
                    ret += numTake * 2
                    if c[word] > 0:
                        center = 1
                else:
                    numTake = min(c[word],c[reverse])
                    c[word] -= numTake
                    c[reverse] -= numTake
                    ret += numTake * 4
        
        return ret + (center * 2)
