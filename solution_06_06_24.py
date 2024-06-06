class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        

        c = Counter(hand)
        min_heap = list(c.keys())
        
        heapq.heapify(min_heap)

        while min_heap:
            current_card = min_heap[0]  # Get the smallest card value
            # Check each consecutive sequence of groupSize cards
            for i in range(groupSize):
                if c[current_card + i] == 0:
                    return False
                c[current_card + i] -= 1
                if c[current_card + i] == 0:
                    if current_card + i != heapq.heappop(min_heap):
                        return False

        return True
