class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        s = {i for i in range(n)}

        for _,d in edges:
            s.discard(d)
        
        if len(s) > 1:
            return -1
        
        return s.pop()
