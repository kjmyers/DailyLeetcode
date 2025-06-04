class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        l = n - numFriends + 1

        ret = ""

        for i in range(n):
            ret = max(ret, word[i:min(i+l, n)])
        
        return ret
