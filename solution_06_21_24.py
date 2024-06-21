class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        unSat = [0] * len(customers)
        ret = 0
        for i in range(len(customers)):
            if grumpy[i] == 1:
                unSat[i] = customers[i]
            else:
                ret += customers[i]

        winSum = sum(unSat[:minutes])
        maxWin = winSum
        for i in range(minutes,len(unSat)):
            winSum += unSat[i]
            winSum -= unSat[i-minutes]
            maxWin = max(maxWin, winSum)

        return ret + maxWin
