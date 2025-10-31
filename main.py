from task import Task
from tasklist import TaskList
VERSION = "v0.1.0"

def main():
    print(f"Welcome to TskTsk {VERSION}!")
    tasklist = TaskList()

    while True:
        cmd = input("> ").lower()
        match (cmd):
            case "list" | "ls":
                print(tasklist)
            case "add" | "a":
                t = Task(input("Name of Task: "))
                tasklist.add_task(t)
            case "quit" | "q":
                print('Quitting...')
                break
            case _:
                print("Invalid command format")

if __name__ == "__main__":
    main()