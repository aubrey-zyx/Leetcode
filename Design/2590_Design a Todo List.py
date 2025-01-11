class Task:
    def __init__(self, taskId, description, due, tags):
        self.taskId = taskId
        self.description = description
        self.due = due
        self.tags = tags
        self.completed = False

class TodoList:

    def __init__(self):
        self.ht = defaultdict(list[Task])
        self.cnt = 0

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        self.cnt += 1
        self.ht[userId].append(Task(self.cnt, taskDescription, dueDate, tags))
        return self.cnt

    def getAllTasks(self, userId: int) -> List[str]:
        res = sorted(self.ht[userId], key=lambda x: x.due)
        return [t.description for t in res if not t.completed]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        res = sorted(self.ht[userId], key=lambda x: x.due)
        return [t.description for t in res if not t.completed and tag in t.tags]

    def completeTask(self, userId: int, taskId: int) -> None:
        for t in self.ht[userId]:
            if t.taskId == taskId:
                t.completed = True
                return


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)