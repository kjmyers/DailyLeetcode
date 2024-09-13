class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pre = 0
        history = [0] * len(arr)
        for i in range(len(arr)):
            pre ^= arr[i]
            history[i] = pre
        
        ret = [0] * len(queries)
        for j in range(len(queries)):
            res = history[queries[j][1]]
            if queries[j][0] > 0:
                res ^= history[queries[j][0]-1]
            ret[j] = res

        return ret
