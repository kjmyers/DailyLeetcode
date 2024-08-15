class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens = 0
        fives = 0
        for c in bills:
            if c == 5:
                fives += 1
            if c == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            if c == 20:
                if fives == 0:
                    return False
                if tens == 0 and fives < 3:
                    return False
                if tens > 0:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
        
        return True
