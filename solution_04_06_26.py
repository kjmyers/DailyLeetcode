class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obsts = set()
        for o in obstacles:
            obsts.add((o[0],o[1]))
        
        posx = 0
        posy = 0
        direct = 0
        directions = ((0,1),(-1,0),(0,-1),(1,0))
        ret = 0

        for c in commands:
            if c == -2:
                direct += 1
                if direct > 3:
                    direct = 0
            elif c == -1:
                direct -= 1
                if direct < 0:
                    direct = 3
            else:
                for _ in range(c):
                    nexX = posx + directions[direct][0]
                    nexY = posy + directions[direct][1]
                    if (nexX, nexY) in obsts:
                        break
                    posx = nexX
                    posy = nexY
            ret = max(ret,posx**2 + posy**2)
                    
        
        return ret
