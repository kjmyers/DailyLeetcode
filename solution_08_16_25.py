class Solution:
    def maximum69Number (self, num: int) -> int:
        ns = str(num)

        for i in range(len(ns)):
            if ns[i] == "6":
                return int(ns[:i] + "9" + ns[i+1:])
        
        return num
