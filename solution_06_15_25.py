class Solution:
    def maxDiff(self, num: int) -> int:
        min_num = str(num)
        max_num = str(num)

        for digit in max_num:
            if digit != "9":
                max_num = max_num.replace(digit, "9")
                break

        for i in range(len(min_num)):
            if i == 0:
                if min_num[i] != "1":
                    min_num = min_num.replace(min_num[i], "1")
                    break
            else:
                if min_num[i] != "0" and min_num[i] != min_num[0]:
                    min_num = min_num.replace(min_num[i], "0")
                    break

        return int(max_num) - int(min_num)
