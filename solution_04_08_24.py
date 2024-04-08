class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud = deque(students)
        sand = deque(sandwiches)

        n = float('inf')

        while stud and len(stud) != n:
            n = len(stud)
            for i in range(n):
                if stud[0] == sand[0]:
                    stud.popleft()
                    sand.popleft()
                else:
                    stud.append(stud.popleft())
        
        return len(stud)
