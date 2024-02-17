class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        for i in range(1,len(heights)):
            if heights[i] > heights[i-1]:
                heappush(q,(heights[i] - heights[i-1]))
            if len(q) <= ladders:
                continue
            bricks -= heappop(q)
            if bricks < 0:
                return i-1
        
        return len(heights) - 1
