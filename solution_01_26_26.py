class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        ret = []
        for i in range(1,len(arr)):
            diff = arr[i] - arr[i-1]
            if diff < minDiff:
                minDiff = diff
                ret = [[arr[i-1], arr[i]]]
            elif diff == minDiff:
                ret.append([arr[i-1], arr[i]])
        
        return ret
