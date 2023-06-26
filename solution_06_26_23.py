class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ret = 0

        left = candidates
        right = len(costs) - candidates - 1

        leftq = costs[:candidates]
        rightq = costs[max(candidates, len(costs) - candidates):]
        
        heapify(leftq)
        heapify(rightq)

        for i in range(k):
            if not rightq or leftq and leftq[0] <= rightq[0]:
                ret += heappop(leftq)
                if left <= right: 
                    heappush(leftq, costs[left])
                    left += 1
            else:
                ret += heappop(rightq)
                if left <= right: 
                    heappush(rightq, costs[right])
                    right -= 1


        return ret
