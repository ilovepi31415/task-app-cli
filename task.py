class Task():
    def __init__(self, title):
        self.__title = title
    
    def __repr__(self):
        return f"[ ] {self.__title}"
    
    def set_title(self, new_title: str) -> None:
        self.__title = new_title
    
    def get_title(self) -> str:
        return self.__title