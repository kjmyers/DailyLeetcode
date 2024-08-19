class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        def solve(screen, clip):
            if screen > n:
                return 1000
            if screen == n:
                return 0
            
            #replace clipboard
            total = 2 + solve(screen + screen, screen)

            #just use clipboard
            total = min(total, 1 + solve(screen + clip, clip))
            return total
        
        return 1 + solve(1,1)
            
