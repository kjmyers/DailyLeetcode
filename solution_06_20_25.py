class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        #dirs = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
        dirs = [0] * 2
        ret = 0

        for i in range(len(s)):
            if s[i] == 'N':
                dirs[0] += 1
            elif s[i] == 'S':
                dirs[0] -= 1
            elif s[i] == 'E':
                dirs[1] += 1
            else: #s[i] == 'W'
                dirs[1] -= 1
            
            ret = max(ret, min(abs(dirs[0]) + abs(dirs[1]) + k * 2, i + 1 ) )
        
        return ret
