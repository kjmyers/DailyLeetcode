class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        returnWords = []
        for word in words:
            for other in words:
                if word in other and other != word and word not in returnWords:
                    returnWords.append(word)
        return returnWords
