class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ret = ""
        count = 1

        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                count += 1
                if count == 3:
                    if ret == "" or ret[0] < num[i]:
                        ret = num[i] * 3
            else:
                count = 1
        
        return ret
