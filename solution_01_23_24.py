class Solution:
    def maxLength(self, arr: List[str]) -> int:
        sets = []
        for a in arr:
            sets.append(set(a))
        
        def backtrack(i, s):
            if i >= len(arr):
                return len(s)
            cur = sets[i]
            ret = 0
            if len(cur) == len(arr[i]) and s - cur == s:
                s |= cur
                ret = backtrack(i+1,s)
                s -= cur
            ret = max(ret, backtrack(i+1,s))
            return ret
        
        return backtrack(0,set())
            

        return 0
