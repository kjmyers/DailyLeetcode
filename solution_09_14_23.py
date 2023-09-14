class Solution:
    def findItinerary(self, tickets):
        def dfs(airport):
            while self.adj_list[airport]:
                candidate = self.adj_list[airport].pop()
                dfs(candidate)
            self.route.append(airport)
        
        self.route = []
        self.adj_list = defaultdict(list)
        for i,j in tickets:
            self.adj_list[i].append(j)
        for key in self.adj_list: 
            self.adj_list[key] = sorted(self.adj_list[key], reverse=True)
            
        dfs("JFK")
        return self.route[::-1]
