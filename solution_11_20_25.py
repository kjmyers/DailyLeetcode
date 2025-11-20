class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:(i[1],-i[0]))
        ret = [intervals[0][1]-1, intervals[0][1]]
        
        for i in intervals[1:]:
            if i[0] <= ret[-2]:
                pass
            elif i[0] > ret[-1]:
                ret.append(i[1]-1)
                ret.append(i[1])
            else:
                ret.append(i[1])
        
        return len(ret)
