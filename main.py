from task import Task
from tasklist import TaskList
VERSION = "v0.1.1"

def main():
    print(f"Welcome to TskTsk {VERSION}!")
    print("Type HELP for a list of commmands")
    tasklist = TaskList()

    while True:
        cmd = input("> ").lower().strip()
        match (cmd):
            case "help" | "h":
                print("LIST: print list of tasks")
                print("ADD : add task to list")
                print("QUIT: quit program")
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