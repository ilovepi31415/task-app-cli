class Task():
    def __init__(self, title):
        self.__title = title
        self.__complete = False
    
    def __repr__(self):
        if self.__complete:
            icon = '*'
        else:
            icon = ' '
        return f"[{icon}] {self.__title}"
    
    def set_title(self, new_title: str) -> None:
        self.__title = new_title
    
    def get_title(self) -> str:
        return self.__title
    
    def mark_complete(self):
        self.__complete = True