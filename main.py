from task import Task
from tasklist import TaskList
VERSION = "v0.3.0"

def main():
    print(f"Welcome to TskTsk {VERSION}!")
    print("Type HELP for a list of commmands")
    
    tasklist = TaskList.from_json()

    while True:
        cmd = input("> ").lower().strip()
        match (cmd):
            # Display the list of commands
            case "help" | "h":
                print("LIST: print list of tasks")
                print("ADD : add task to list")
                print("Complete: mark a task as complete")
                print("DELETE: remove task from list")
                print("QUIT: quit program")
            # Print the tasks in the task list
            case "list" | "l":
                print(tasklist)
            # Add a new task to the task list
            case "add" | "a":
                title = Task(input("Name of task: "))
                tasklist.add_task(title)
            # Update the title of a task
            case "edit" | "e":
                title = input("Name of task: ")
                new_title = input("New title: ")
                tasklist.get_task(title).set_title(new_title)
            # Remove a task from the task list
            case "delete" | "d":
                title = input("Task to remove: ")
                tasklist.remove_task(title)
            # Mark a task as complete
            case "complete" | "c":
                title = input("Name of task: ")
                tasklist.get_task(title).mark_complete()
            # Quit the program after saving
            case "quit" | "q":
                print("Saving...")
                tasklist.to_json()
                print("Quitting...")
                break
            case _:
                print("Invalid command format")

if __name__ == "__main__":
    main()