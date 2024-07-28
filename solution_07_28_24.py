class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        # dist1[i] stores the minimum time taken to reach node i from node 1. dist2[i] stores the
        # second minimum time taken to reach node from node 1. freq[i] stores the number of times a
        # node is popped out of the heap.
        dist1 = [float('inf')] * (n+1)
        dist2 = [float('inf')] * (n+1)
        freq = [0] * (n+1)
        min_heap = []
        heappush(min_heap, (0,1))
        dist1[1] = 0

        while min_heap:
            timeTaken, node = heappop(min_heap)
            freq[node] += 1
            # If the node is being visited for the second time and is 'n', return the answer.
            if freq[node] == 2 and node == n:
                # If the current light is red, wait till the path turns green.
                return timeTaken
            if (timeTaken // change) % 2:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken = timeTaken + time
            
            for neighbor in adj[node]:
                # Ignore nodes that have already popped out twice.
                if freq[neighbor] == 2:
                    continue
                # Update dist1 if it's more than the current timeTaken and store its value in
                # dist2 since that becomes the second minimum value now.
                if dist1[neighbor] > timeTaken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = timeTaken
                    heappush(min_heap, (timeTaken, neighbor))
                elif dist2[neighbor] > timeTaken and dist1[neighbor] != timeTaken:
                    dist2[neighbor] = timeTaken
                    heappush(min_heap, (timeTaken, neighbor))

        return 0
