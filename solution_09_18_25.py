class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.m = {}
        self.h = []
        self.o = {}
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.m[taskId] = priority
        self.o[taskId] = userId
        heappush(self.h, (-priority, -taskId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.m[taskId] = newPriority
        heappush(self.h, (-newPriority, -taskId))
    

    def rmv(self, taskId: int) -> None:
        self.m[taskId] = None

    def execTop(self) -> int:
        while self.h:
            priority, taskId = heappop(self.h)
            priority = -priority
            taskId = -taskId
            if self.m[taskId] == priority:
                self.m[taskId] = None
                return self.o.get(taskId, -1)
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
