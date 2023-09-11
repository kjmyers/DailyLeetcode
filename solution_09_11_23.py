class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        d = defaultdict(list)
        n = len(groupSizes)
        ret = []

        for i in range(n):
            d[groupSizes[i]].append(i)
            if len(d[groupSizes[i]]) == groupSizes[i]:
                ret.append(d[groupSizes[i]])
                d[groupSizes[i]] = []
        
        return ret
