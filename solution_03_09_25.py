class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ret = 0
        altCount = 1
        last = colors[0]

        for i in range(1,len(colors)):
            if colors[i] == last:
                altCount = 1
                last = colors[i]
                continue
            
            altCount += 1

            if altCount >= k:
                ret += 1
            last = colors[i]
        
        for i in range(k-1):
            if colors[i] == last:
                break
            altCount += 1
            if altCount >= k:
                ret += 1
            
            last = colors[i]

        return ret
