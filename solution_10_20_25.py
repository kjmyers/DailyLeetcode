class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ret = 0
        for o in operations:
            if o[1] == "+":
                ret += 1
            else:
                ret -= 1
        return ret
