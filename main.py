# DONE apart from exception handling 
import pickle
from pathlib import Path

# make directory to store app data
APP_DIR = Path.home() / "ToDoListApp"
DATA_DIR = APP_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

TO_DO_LIST = DATA_DIR / "todolist.dat"

# Function for the user to input the tasks to create a todo list and store it in a binary file
def set_tasks():
    todo = {}
    more = "y"
    while more.lower() == "y":
        task = input("Enter today's tasks to be added in to do list: ")
        todo[task] = "Pending"
        more = input("Add more tasks?[y/n]: ")
        # To ensure that the user enters a valid input for more tasks
        while more.lower() not in ("y", "n"):
            print("Please enter a valid input!\n")
            more = input("Add more tasks?[y/n]: ")
        print()
    
    with open(TO_DO_LIST, "wb") as f:
        pickle.dump(todo, f)
    
    # Displays the tasks in neat formatting
    print("Today's tasks are: ")
    show_tasks()

# Displays the tasks along with their status
def show_tasks():
    try:
        with open(TO_DO_LIST, "rb") as f:
            todo = pickle.load(f)
    except FileNotFoundError:
        print("Yet to be set!\n")
        return
    if todo == {}:
        print("Yet to be set!\n")
        return
    i = 1
    for key in todo:
        print(f"{i}. {key} -> Status: {todo[key]}")
        i = i+1 
    print()

# Function to ask the user to update the status of a task
def update_task_status():
    try:
        with open(TO_DO_LIST, "rb") as f:
            todo = pickle.load(f)
    except FileNotFoundError:
        print("Your to do list is empty!\n")
        return
    
    if todo == {}:
        print("Your to do list is empty!\n")
        return
    
    print("The current status of today's tasks is: ")
    show_tasks()

    for key in todo:
        update = input(f"Enter the status of the task - {key} [Done/Pending]: ")
        if update.lower() == "done":
            todo[key] = "Done"
        elif update.lower() == "pending":
            todo[key] = "Pending"
        else:
            print(f"Please enter a valid status for your task - {key}")
        print()
    
    with open(TO_DO_LIST, "wb") as f:
        pickle.dump(todo, f)

    print(f"Your updated to do list is: ")
    show_tasks() 

# give options to remove existing tasks, add new tasks, and change existing ones
# Below three functions are intended for the same

def remove_task():
    try:
        with open(TO_DO_LIST, "rb") as f:
            todo = pickle.load(f)
    except FileNotFoundError:
        print("Your to do list is empty!\n")
        return
    if todo == {}:
        print("Your to do list is empty!\n")
        return
    
    tasks = list(todo.keys())
    
    print(f"Your current tasks are: ")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
    
    n = int(input("To remove a task enter it's index no. : "))
    print()
    try:
        if n in range(1, (len(tasks)+1)):
            task = tasks[n-1]
            del todo[task]
            with open(TO_DO_LIST, "wb") as f:
                pickle.dump(todo, f)
            print("Task removed successfully!")
        else:
            print("Please enter a valid index!")
    except Exception:
        print("Error!")
    print()
    

def add_task():
    try:
        with open(TO_DO_LIST, "rb") as f:
            todo = pickle.load(f)
    except FileNotFoundError:
        print("Please create a to do list first!\n")
        return
    
    task = input("Enter new task: ")
    todo[task] = "Pending"
    with open(TO_DO_LIST, "wb") as f:
        pickle.dump(todo, f)
    
    print("Today's updated tasks are: ")
    i = 1
    for key in todo:
        print(f"{i}. {key} -> Status: {todo[key]}")
        i = i+1  

    

def change_task():
    try:
        with open(TO_DO_LIST, "rb") as f:
            todo = pickle.load(f)
    except FileNotFoundError:
        print("Please create a to do list first!\n")
        return
    tasks = list(todo.keys())
    
    print(f"Your current tasks are: ")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
    
    n = int(input("To update a task enter it's index no. : "))
    new_task = input("Enter the new task: ")

    try:
        tasks.remove(tasks[n-1])
        tasks.insert(n-1, new_task)
        todo_new = {}
        for task in tasks:
            if task in todo:
                todo_new[task] = todo[task]
            else:
                todo_new[task] = "Pending"

        with open(TO_DO_LIST, "wb") as f:
            pickle.dump(todo_new, f)
        print("Task updated successfully!")
    except Exception:
        print("Error!")


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