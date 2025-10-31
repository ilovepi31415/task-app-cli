from task import Task
from tasklist import TaskList
VERSION = "v0.2.0"

def main():
    print(f"Welcome to TskTsk {VERSION}!")
    print("Type HELP for a list of commmands")
    tasklist = TaskList()

    while True:
        cmd = input("> ").lower().strip()
        match (cmd):
            # Display the list of commands
            case "help" | "h":
                print("LIST: print list of tasks")
                print("ADD : add task to list")
                print("QUIT: quit program")
            # Print the tasks in the task list
            case "list" | "l":
                print(tasklist)
            # Add a new task to the task list
            case "add" | "a":
                title = Task(input("Name of task: "))
                tasklist.add_task(title)
            # Remove a task from the task list
            case "edit" | "c":
                title = input("Name of task: ")
                new_title = input("New title: ")
                tasklist.get_task(title).set_title(new_title)
            case "delete" | "d":
                title = input("Task to remove: ")
                tasklist.remove_task(title)
            # Quit the program
            case "quit" | "q":
                print('Quitting...')
                break
            case _:
                print("Invalid command format")

if __name__ == "__main__":
    main()