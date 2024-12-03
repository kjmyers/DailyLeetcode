class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ret = []
        spacesi = 0
        for i in range(len(s)):
            if spacesi < len(spaces) and i == spaces[spacesi]:
                ret.append(" ")
                spacesi += 1
            ret.append(s[i])
        
        return "".join(ret)
