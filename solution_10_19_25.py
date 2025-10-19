class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        q = deque()
        q.append(s)
        seen = set()
        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            q.append("".join(cur[b:] + cur[:b]))

            add = ""
            for i in range(n):
                if i % 2 == 0:
                    add += cur[i]
                else:
                    add += ( str((int(cur[i]) + a) % 10) )
            q.append(add)
        
        return min(seen)
