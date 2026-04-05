class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0

        for m in moves:
            if m == 'U':
                x += 1
            elif m == 'D':
                x -= 1
            elif m == 'R':
                y += 1
            elif m == 'L':
                y -= 1
        
        if x == 0 and y ==0:
            return True
        return False
