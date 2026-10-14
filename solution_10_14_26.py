class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num*9:
            return ""
        
        digits = [0] * num
        i = 0
        while sum > 8:
            digits[i] = 9
            sum -= 9
            i += 1
        if sum > 0:
            digits[i] = sum

        return "".join(map(str, digits))
