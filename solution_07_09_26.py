class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        groups = [0] * n
        curGroup = 0

        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                curGroup += 1
            groups[i] = curGroup
        
        ret = [False] * len(queries)
        for i in range(len(queries)):
            start, end = queries[i]
            if groups[start] == groups[end]:
                ret[i] = True
        
        return ret
