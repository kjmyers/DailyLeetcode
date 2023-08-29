class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yCount = 0
        for i in range(len(customers)):
            if customers[i] == "Y":
                yCount += 1
        
        ret = 0
        minVal = yCount

        for i in range(len(customers)):
            if yCount < minVal:
                ret = i
                minVal = yCount
            
            if customers[i] == "Y":
                yCount -= 1
            else:
                yCount += 1            
        
        if yCount < minVal:
            ret = len(customers)
            minVal = yCount
        return ret
