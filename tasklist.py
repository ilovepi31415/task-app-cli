from task import Task
import os
import json

class TaskList():
    def __init__(self, tasks = []):
        self.tasks: list[Task] = tasks
    
    @staticmethod
    def from_json():
        tasklist = TaskList()
        try:
            with open("tasklist.json", 'r') as f:
                task_dict = json.load(f)
                for task in task_dict:
                    tasklist.add_task(Task.from_dict(task, task_dict[task]))
        except FileNotFoundError:
            pass
        return tasklist

    
    def __repr__(self):
        repr = "Task List:"
        for task in self.tasks:
            repr += f"\n{task}"
        return repr
    
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
    
    def get_task(self, title: str) -> Task:
        try:
            partial_match = []
            for task in self.tasks:
                if task.get_title() == title:
                    return task
                # If only one partial match, autocomplete the title
                elif task.get_title().startswith(title):
                    partial_match.append(task)
            if len(partial_match) == 1:
                return partial_match[0]
            raise Exception(f"Task {title} not found")
        except Exception as e:
            print(e)

    def remove_task(self, title: str) -> None:
        task = self.get_task(title)
        if task:
            self.tasks.remove(task)
    
    def to_json(self):
        json_dict = {}
        for task in self.tasks:
            json_dict[task.get_title()] = task.to_json()
        tasks_json = json.dumps(json_dict)
        with open("tasklist.json", 'w') as f:
            f.write(tasks_json)