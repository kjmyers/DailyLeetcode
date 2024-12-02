class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentList = sentence.split(" ")
        for i in range(len(sentList)):
            if len(searchWord) <= len(sentList[i]):
                if sentList[i][:len(searchWord)] == searchWord:
                    return i + 1
        
        return -1
