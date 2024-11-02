class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sList = sentence.split()

        for i in range(1,len(sList)):
            if sList[i][0] != sList[i-1][-1]:
                return False
        if sList[0][0] != sList[-1][-1]:
            return False
        
        return True
