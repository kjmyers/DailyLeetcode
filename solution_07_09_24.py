class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curTime = customers[0][0]
        curCust = 0
        waitTime = 0

        for enterTime, cookTime in customers:
            if curTime < enterTime:
                curTime = enterTime
            curTime += cookTime
            waitTime += curTime - enterTime
        
        return waitTime / len(customers)
