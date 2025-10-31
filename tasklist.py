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
    
    def get_task(self, title: str) -> Task:
        try:
            for task in self.list:
                if task.get_title() == title:
                    return task
            raise Exception(f"Task {title} not found")
        except Exception as e:
            print(e)

    def remove_task(self, title: str) -> None:
        try:
            for task in self.list:
                if task.get_title() == title:
                    self.list.remove(task)
                    return
            raise Exception(f"Task {title} not in list")
        except Exception as e:
            print(e)