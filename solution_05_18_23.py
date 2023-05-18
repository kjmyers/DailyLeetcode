class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        ret = []

        graph = {}
        for e in edges:
            graph[e[1]] = e[0]
        
        for i in range(n):
            if i not in graph.keys():
                ret.append(i)
        
        return ret
