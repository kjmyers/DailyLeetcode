class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            big = heapq.heappop(stones)
            small = heapq.heappop(stones)
            if big != small:
                heapq.heappush(stones,big-small)

        if stones:
            return -stones[0]
        else:
            return 0
