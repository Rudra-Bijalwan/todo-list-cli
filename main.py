# DONE apart from exception handling 
import json
from pathlib import Path

# make directory to store app data
APP_DIR = Path.home() / "ToDoListApp"
DATA_DIR = APP_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

TO_DO_LIST = DATA_DIR / "todolist.json"

# load contents of the to do list json file
def load_file():
    if not TO_DO_LIST.exists():
        return []
    
    with open(TO_DO_LIST, 'r') as f:
        return json.load(f)
    
# save the todo list
def save_file(todo_list: list):
    with open(TO_DO_LIST, 'w') as f:
        json.dump(todo_list, f, indent=2)

# Function for the user to input the tasks to create a todo list and store it in a binary file
def set_tasks():
    todo_list = []
    more = "y"
    while more.lower() == "y":
        task = input("Enter today's tasks to be added in to do list: ")
        task_data = {}
        task_data["task"] = task
        task_data["status"] = "Pending"
        todo_list.append(task_data)

        more = input("Add more tasks?[y/n]: ")
        # To ensure that the user enters a valid input for more tasks
        while more.lower() not in ("y", "n"):
            print("Please enter a valid input!\n")
            more = input("Add more tasks?[y/n]: ")
        print()

    save_file(todo_list)

    # Displays the tasks in neat formatting
    print("Today's tasks are: ")
    show_tasks()

# Displays the tasks along with their status
def show_tasks():
    todo_list = load_file()

    if todo_list == []:
        print("Tasks are yet to be set!\n")
        return
    
    i = 1
    for task_data in todo_list:
        print(f"{i}. {task_data["task"]} -> Status: {task_data["status"]}")
        i = i+1 
    print()

# Function to ask the user to update the status of a task
def update_task_status():
    todo_list = load_file()
    
    if todo_list == []:
        print("Your to do list is empty!\n")
        return
    
    print("The current status of today's tasks is: ")
    show_tasks()

    more = 'y'
    while more.lower() == 'y':
        try:
            n = int(input("Enter the index number of the task whose status is to be changed: "))
            if n not in range(1,len(todo_list)+1):
                print("Please enter a valid index!\n")
                return
        except ValueError:
            print("Please enter a valid index!\n")
            return
        index = n - 1

        update = input(f"Enter the status of the task - {todo_list[index]["task"]} [Done/Pending]: ")
        if update.lower() == "done":
            todo_list[index]["status"] = "Done"
        elif update.lower() == "pending":
            todo_list[index]["status"] = "Pending"
        else:
            print(f"Please enter a valid status for your task - {todo_list[index]["task"]}\n")
            return
        print()
        
        save_file(todo_list)
        print("Task status updated.\n")

        while True:
            more = input("Update more tasks? [y/n] ")

            if more.lower() not in ('y', 'n'):
                print("Please enter a valid answer [y/n]!\n")
            else:
                break
        print()

    print(f"Your updated to do list is: ")
    show_tasks() 

# remove existing tasks
def remove_task():
    todo_list = load_file()

    if todo_list == []:
        print("Your to do list is empty!\n")
        return
    
    print(f"Your current tasks are: ")
    for i in range(len(todo_list)):
        print(f"{i+1}. {todo_list[i]["task"]}")
    
    index = int(input("To remove a task enter it's index no. : "))
    print()
        
    if index in range(1, (len(todo_list)+1)):
        del todo_list[index-1]

        save_file(todo_list)
        print("Task removed successfully!")
    else:
        print("Please enter a valid index!")

    print()
    
# add new tasks to existing to do list
def add_task():
    todo_list = load_file()
    
    task = input("Enter new task: ")
    print()

    task_data = {"task": task, "status": "Pending"}
    todo_list.append(task_data)

    save_file(todo_list)
    print("Task added.\n")

# change existing task
def change_task():
    todo_list = load_file()
    
    print(f"Your current tasks are: ")
    for i in range(len(todo_list)):
        print(f"{i+1}. {todo_list[i]["task"]}")
    
    index = int(input("To update a task enter it's index no. : "))
    if index not in range(1,len(todo_list)+1):
        print("Please enter a valid index!")
        print()
        return
    
    new_task = input("Enter the new task: ")
    print()

    new_task_data = {"task": new_task, "status": "Pending"}
    todo_list[index-1] = new_task_data

    save_file(todo_list)
    print("Task updated successfully!")


if __name__ == "__main__":
    print("Hello, user! Enter the indices as per the below instructions to use the app: \n")
    while True:
        # To ask the user to select and execute one of the options
        try:
            n= int(input('''Select:\n1. To set tasks and create a new todo list
2. To show the To Do List created by the user
3. To update the status of task(s)
4. To remove a task
5. To add a task
6. To change a task
7. Exit\n'''))
            print()

            if n == 1:
                set_tasks()
            elif n == 2:
                print("Today's tasks are:\n")
                show_tasks()
            elif n == 3:
                update_task_status()
            elif n == 4:
                remove_task()
            elif n == 5:
                add_task()
            elif n == 6:
                change_task()
            elif n == 7:
                break
            # To ensure that the user enters a valid input for selecting an option
            else:
                print("Please enter an integer from the given options!\n")
        
        except ValueError:
            print("Please enter an integer from the given options!\n")