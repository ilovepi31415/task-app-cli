from task import Task
from tasklist import TaskList
VERSION = "v0.3.2"

def main():
    print(f"Welcome to TskTsk {VERSION}!")
    print("Type HELP for a list of commmands")
    
    tasklist = TaskList.from_json()

    while True:
        # Split the input to allow for quick commands
        s = input("> ").lower().strip().split(maxsplit=1)
        cmd = s[0]
        if len(s) > 1:
            body = s[1]
        else:
            body = None

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
                if body:
                    title = body
                else:
                    title = input("Name of task: ")
                tasklist.add_task(Task(title))
            # Update the title of a task
            case "edit" | "e":
                if body:
                    title = body
                else:
                    title = input("Name of task: ")
                new_title = input("New title: ")
                task = tasklist.get_task(title)
                if task:
                    task.set_title(new_title)
            # Remove a task from the task list
            case "delete" | "d":
                if body:
                    title = body
                else:
                    title = input("Task to remove: ")
                tasklist.remove_task(title)
            # Mark a task as complete
            case "complete" | "c":
                if body:
                    title = body
                else:
                    title = input("Name of task: ")
                task = tasklist.get_task(title)
                if task:
                    task.mark_complete()
            # Save the tasklist without quititing
            case "save" | "s":
                tasklist.to_json()
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