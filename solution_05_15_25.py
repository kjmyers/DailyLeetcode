class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        prevG = 1
        curRet = []
        ret = []
        for i in range(len(groups)):
            if groups[i] != prevG:
                prevG = groups[i]
                curRet.append(words[i])
        
        ret = curRet
        curRet = []
        prevG = 0
        for i in range(len(groups)):
            if groups[i] != prevG:
                prevG = groups[i]
                curRet.append(words[i])
        
        if len(curRet) > len(ret):
            return curRet

        return ret
