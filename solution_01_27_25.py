class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = {i: [] for i in range(numCourses)}
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        
        
        def isPreq(pre, course, visited):
            visited.add(course)
            if course == pre:
                return True
            for c in graph[course]:
                if c not in visited:
                    if isPreq(pre, c, visited):
                        return True
            
            return False

        ret = []

        for pre, course in queries:
            visited = set()
            ret.append(isPreq(pre,course, visited))
        
        return ret
