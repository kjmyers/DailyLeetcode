class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sortedArr = sorted(arr)

        d = {}
        i = 1
        for v in sortedArr:
            if v not in d:
                d[v] = i
                i += 1
        
        ret = [0] * len(arr)
        for i in range(len(arr)):
            ret[i] = d[arr[i]]

        return ret
