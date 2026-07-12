# some good additions to make:
# make the data structure to store tasks in only tasks.json file, and it has tasks for all the dates.
# make the program get meaningful insights from all tasks data
import json
from datetime import date
from pathlib import Path

# make directory to store app data
APP_DIR = Path.home() / "ToDoListApp"
DATA_DIR = APP_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

ALL_TASKS = DATA_DIR / "tasks.json"

# load contents of the to do list json file
def load_file(file: Path):
    if not file.exists():
        return []
    
    with open(file, 'r') as f:
        return json.load(f)
    
# save the todo list
def save_file(all_tasks: list, file: Path):
    with open(file, 'w') as f:
        json.dump(all_tasks, f, indent=2)

# Function for the user to input the tasks for the current date and store it in a json file
def set_tasks():

    more = "y"
    # if user wants to add more tasks
    while more.lower() == "y":
        task = input("Enter today's tasks to be added in to do list: ")
        task_data = {}
        task_data["task"] = task
        task_data["status"] = "Pending"
        task_data["date"] = current_date

        task_file.append(task_data)

        more = input("Add more tasks?[y/n]: ")
        # To ensure that the user enters a valid input for more tasks
        while more.lower() not in ("y", "n"):
            print("Please enter a valid input!\n")
            more = input("Add more tasks?[y/n]: ")
        print()

    save_file(task_file, ALL_TASKS)
    print("Tasks saved!\n")

# Displays the tasks along with their status
def show_tasks():
    
    # if todays tasks not set
    if today_tasks == []:
        print("Tasks are yet to be set!\n")
        return
    
    i = 1
    for task_data in today_tasks:
        print(f"{i}. {task_data["task"]} -> Status: {task_data["status"]}")
        i = i+1 
    print()

# Function to ask the user to update the status of a task
def update_task_status():
    
    if today_tasks == []:
        print("Your to do list is empty!\n")
        return
    
    print("The current status of today's tasks is: ")
    show_tasks()

    more = 'y'
    while more.lower() == 'y':
        try:
            n = int(input("Enter the index number of the task whose status is to be changed: "))
            if n not in range(1,len(today_tasks)+1):
                print("Please enter a valid index!\n")
                return
        except ValueError:
            print("Please enter a valid index!\n")
            return
        index = n - 1

        update = input(f"Enter the status of the task - {today_tasks[index]["task"]} [Done/Pending]: ")
        if update.lower() == "done":
            today_tasks[index]["status"] = "Done"
        elif update.lower() == "pending":
            today_tasks[index]["status"] = "Pending"
        else:
            print(f"Please enter a valid status for your task - {today_tasks[index]["task"]}\n")
            return
        print()
        
        save_file(task_file, ALL_TASKS)
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

    if today_tasks == []:
        print("Your to do list is empty!\n")
        return
    
    print(f"Your current tasks are: ")
    for i in range(len(today_tasks)):
        print(f"{i+1}. {today_tasks[i]["task"]}")
    
    n = int(input("To remove a task enter it's index no. : "))
    index = n - 1
    print()
        
    if index in range(len(today_tasks)):
        # remove the task
        task_file.remove(today_tasks[index])
        save_file(task_file, ALL_TASKS)

        print("Task removed successfully!")
    else:
        print("Please enter a valid index!")

    print()

# change existing task
def change_task():
    
    print(f"Your current tasks are: ")
    for i in range(len(today_tasks)):
        print(f"{i+1}. {today_tasks[i]["task"]}")
    
    n = int(input("To update a task enter it's index no. : "))
    index = n - 1

    if index not in range(len(today_tasks)):
        print("Please enter a valid index!")
        print()
        return
 
    new_task = input("Enter the new task: ")
    print()

    today_tasks[index]["task"] = new_task
    
    save_file(task_file, ALL_TASKS)
    print("Task updated successfully!\n")

if __name__ == "__main__":

    print("Hello, user! Enter the indices as per the below instructions to use the app: \n")
    while True:
        # store current date
        current_date = date.today().strftime("%d/%m/%Y")
        task_file = load_file(ALL_TASKS)

        # store today's to do list
        today_tasks = [tasks 
                   for tasks in task_file
                   if tasks["date"] == current_date]
        
        # To ask the user to select and execute one of the options
        try:
            n= int(input('''Select:\n1. To set tasks / add more tasks to the to do list
2. To show today's tasks
3. To update the status of task(s)
4. To remove a task
5. To change a task
6. Exit\n'''))
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
                change_task()
            elif n == 6:
                break
            # To ensure that the user enters a valid input for selecting an option
            else:
                print("Please enter an integer from the given options!\n")
        
        except ValueError:
            print("Please enter an integer from the given options!\n")