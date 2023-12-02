class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = dict(Counter(chars))
        ret = 0

        for word in words:
            dcur = dict(d)
            n = len(word)
            for i in range(n):
                if word[i] not in dcur or dcur[word[i]] == 0:
                    break
                dcur[word[i]] -= 1
                if i == n-1:
                    ret += n
        
        return ret
