class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        #Graph the bombs

        n = len(bombs)

        graph = defaultdict(list)

        for i in range(n):
            for j in range(i+1,n):
                dist = sqrt( (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2 )
                #print(i,j,dist,bombs[i][2])
                if dist <= bombs[i][2]:
                    graph[i].append(j)
                if dist <= bombs[j][2]:
                    graph[j].append(i)
        
        #print(graph)

        seen = set()
        def dfs(node):
            seen.add(node)
            nextNodes = graph[node]
            ret = 0

            for n in nextNodes:
                if n not in seen:
                    ret += dfs(n)
            
            return ret + 1
        

        ret = 0

        for b in range(len(bombs)):
            ret = max(ret, dfs(b))
            seen = set()
        
        return ret
