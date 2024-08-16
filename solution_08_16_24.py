class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        vmin, vmax = float('inf'), -float('inf')
        for arr in arrays:
            ans = max(ans, vmax - arr[0], arr[-1] - vmin)
            vmin = min(vmin, arr[0])
            vmax = max(vmax, arr[-1])
        return ans
