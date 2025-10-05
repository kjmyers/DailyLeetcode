class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nr = len(heights)
        nc = len(heights[0])

        def bfs(queue):
            reachable = set()
            while queue:
                row, col = queue.popleft()
                # This cell is reachable, so mark it
                reachable.add((row, col))
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # Check all 4 directions
                    new_row, new_col = row + x, col + y
                    # Check if the new cell is within bounds
                    if new_row < 0 or new_row >= nr or new_col < 0 or new_col >= nc:
                        continue
                    # Check that the new cell hasn't already been visited
                    if (new_row, new_col) in reachable:
                        continue
                    # Check that the new cell has a higher or equal height,
                    # So that water can flow from the new cell to the old cell
                    if heights[new_row][new_col] < heights[row][col]:
                        continue
                    # If we've gotten this far, that means the new cell is reachable
                    queue.append((new_row, new_col))
            return reachable

        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(nr):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, nc - 1))
        for i in range(nc):
            pacific_queue.append((0, i))
            atlantic_queue.append((nr - 1, i))
        
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))
        
