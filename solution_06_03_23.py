class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = defaultdict(list)

        for m in range(len(manager)):
            graph[manager[m]].append(m)
        
        #print(graph)

        self.ret = 0

        def dfs(node, time):
            curEmps = graph[node]
            if not curEmps:
                self.ret = max(self.ret, time)
            
            for e in curEmps:
                dfs(e, time + informTime[node])

        dfs(headID,0)

        return self.ret
