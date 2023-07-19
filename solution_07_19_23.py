class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        ans = 0
        k = -inf
        
        for start, end in intervals:
            if start >= k:
                # Case 1
                k = end
            else:
                # Case 2
                ans += 1
        
        return ans
