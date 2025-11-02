class Task():
    def __init__(self, title, complete = False, progress = 0):
        self.__title = title
        self.__complete = complete
        self.__progress = progress 

    def __repr__(self):
        if self.__complete:
            icon = '*'
        else:
            icon = ' '
        progress_bar = ''
        if self.__progress:
            progress_bar = f"[{(self.__progress // 10 * '=').ljust(10)}]"
        return f"[{icon}] {self.__title.ljust(15)} {progress_bar}"
    
    @staticmethod
    def from_dict(task, task_dict):
        new_task = Task(task, task_dict["complete"], task_dict["progress"])
        return new_task
    
    def set_title(self, new_title: str) -> None:
        self.__title = new_title
    
    def get_title(self) -> str:
        return self.__title
    
    def set_progress(self, new_progress: int) -> None:
        if new_progress <= 100 and new_progress >= 0:
            self.__progress = new_progress
    
    def mark_complete(self):
        self.__complete = True

    def to_json(self):
        return {"complete": self.__complete, "progress": self.__progress}