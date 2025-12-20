class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ret = 0
        for i in range(len(strs[0])):
            s = [row[i] for row in strs]
            if sorted("".join(s)) != s:
                ret += 1
            
        return ret
