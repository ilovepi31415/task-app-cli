from task import Task

class TaskList():
    def __init__(self):
        self.list: list[Task] = []
    
    def __repr__(self):
        repr = "Task List:"
        for task in self.list:
            repr += f"\n{task}"
        return repr
    
    def add_task(self, task: Task) -> None:
        self.list.append(task)