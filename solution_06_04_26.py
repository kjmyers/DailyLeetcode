class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ret = 0
        for num in range(num1, num2+1):
            snum = str(num)
            n = len(snum)
            if n < 3:
                continue
            for i in range(1,n-1):
                if  ((snum[i] > snum[i-1] and snum[i] > snum[i+1]) or
                    (snum[i] < snum[i-1] and snum[i] < snum[i+1])):
                    ret += 1
        return ret
