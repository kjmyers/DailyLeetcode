class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        d = deque([i for i in senate])

        rSkip = 0
        dSkip = 0
        while len(set(d)) > 1:
            cur = d.popleft()
            if cur == "R":
                if not rSkip:
                    dSkip += 1
                    d.append(cur)
                else:
                    rSkip -= 1
            
            elif cur == "D":
                if not dSkip:
                    rSkip += 1
                    d.append(cur)
                else:
                    dSkip -= 1
        
        if d[0] == "R":
            return "Radiant"
        else:
            return "Dire"
