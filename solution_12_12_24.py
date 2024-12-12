class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]

        heapify(gifts)

        for _ in range(k):
            cur = -heappop(gifts)
            heappush(gifts,-floor(sqrt(cur)))
        return -sum(gifts)
