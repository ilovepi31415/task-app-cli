class Task():
    def __init__(self, title, complete = False):
        self.__title = title
        self.__complete = complete
    
    def __repr__(self):
        if self.__complete:
            icon = '*'
        else:
            icon = ' '
        return f"[{icon}] {self.__title}"
    
    @staticmethod
    def from_dict(task, task_dict):
        new_task = Task(task, task_dict["complete"])
        return new_task
    
    def set_title(self, new_title: str) -> None:
        self.__title = new_title
    
    def get_title(self) -> str:
        return self.__title
    
    def mark_complete(self):
        self.__complete = True

    def to_json(self):
        return {"complete": self.__complete}