class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                heappush(h, (arr[i]/arr[j], [arr[i],arr[j]]))
        
        for i in range(k-1):
            heappop(h)
        
        _, ret = heappop(h)

        return ret
