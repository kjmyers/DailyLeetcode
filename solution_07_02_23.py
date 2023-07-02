class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        self.indegree = [0] * n
        self.answer = 0
        
        def maxRequest(index, count):
            if index == len(requests):
                for i in range(n):
                    if self.indegree[i]:
                        return
                
                self.answer = max(self.answer, count)
                return
            
            self.indegree[requests[index][0]] -= 1
            self.indegree[requests[index][1]] += 1

            maxRequest(index + 1, count + 1)

            self.indegree[requests[index][0]] += 1
            self.indegree[requests[index][1]] -= 1

            maxRequest(index + 1, count)
        
        maxRequest(0, 0)

        return self.answer
