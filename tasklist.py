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
            for task in self.tasks:
                if task.get_title() == title:
                    return task
            raise Exception(f"Task {title} not found")
        except Exception as e:
            print(e)

    def remove_task(self, title: str) -> None:
        try:
            for task in self.tasks:
                if task.get_title() == title:
                    self.tasks.remove(task)
                    return
            raise Exception(f"Task {title} not in list")
        except Exception as e:
            print(e)
    
    def to_json(self):
        json_dict = {}
        for task in self.tasks:
            json_dict[task.get_title()] = task.to_json()
        tasks_json = json.dumps(json_dict)
        with open("tasklist.json", 'w') as f:
            f.write(tasks_json)