class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = 0

        while numBottles >= numExchange:
            consumed_bottles += numExchange
            numBottles -= numExchange
            numBottles += 1
            numExchange +=1

        return consumed_bottles + numBottles
