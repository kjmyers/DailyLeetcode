class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        
        total = set()
        def rec(i, total): # return set of OR results
            ret = set()
            ret.add(arr[i])
            if i < len(arr) - 1:
                nex = rec(i+1, total)
                for num in nex:
                    ret.add(arr[i] | num)
            
            total |= ret
            return ret
        
        rec(0,total)
        return len(total)
