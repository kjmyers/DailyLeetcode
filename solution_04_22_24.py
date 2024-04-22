class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        q = deque()
        q.append("0000")
        deadendsSet = set(deadends)
        turns = 0
        
        if "0000" in deadendsSet:
            return -1
        
        deadendsSet.add("0000")

        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                if cur == target:
                    return turns

                for i in range(4):
                    val = int(cur[i])+1
                    if val > 9:
                        val -= 10
                    nex = cur[:i] + str(val) + cur[i+1:]
                    if nex not in deadendsSet:
                        q.append(nex)
                        deadendsSet.add(nex)
                    
                    val = int(cur[i])-1
                    if val < 0:
                        val += 10
                    nex = cur[:i] + str(val) + cur[i+1:]
                    if nex not in deadendsSet:
                        q.append(nex)
                        deadendsSet.add(nex)
            turns += 1
        
        return -1
