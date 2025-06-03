class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque()
        locked = set()
        curKeys = set()
        ret = 0
        for box in initialBoxes:
            if status[box] == 0:
                locked.add(box)
            else:
                q.append(box)
        
        while q:
            cur = q.popleft()
            ret += candies[cur]
            for k in keys[cur]:
                curKeys.add(k)
            for box in containedBoxes[cur]:
                if status[box] == 0:
                    locked.add(box)
                else:
                    q.append(box)
                
            for k in curKeys:
                if k in locked:
                    q.append(k)
                    locked.remove(k)


        return ret
