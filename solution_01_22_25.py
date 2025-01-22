class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        cols = len(isWater[0])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        heights = [[-1 for _ in range(cols)] for _ in range(rows)]

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    q.append((r,c))
                    heights[r][c] = 0
        
        nextHeight = 1

        while q:
            layer_size = len(q)

            for _ in range(layer_size):
                cur = q.popleft()

                for d in range(4):
                    nextR = cur[0] + dx[d]
                    nextC = cur[1] + dy[d]

                    if (0 <= nextR < rows and 0 <= nextC < cols) and heights[nextR][nextC] == -1:
                        heights[nextR][nextC] = nextHeight
                        q.append((nextR,nextC))
            nextHeight += 1
        
        return heights
