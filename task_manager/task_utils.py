from datetime import datetime

# Import validation functions
None

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    for index in range(len(tasks)):
        if tasks[index-1]["completed"]==False:
            print(f"{index}. {tasks[index]['title']} - Due: {tasks[index]['due_date']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
   incomplete = 0
   for index in range(len(tasks)):
        if tasks[index-1]["completed"]==False:
            incomplete += 1
            progress =len(tasks) - incomplete / len(tasks) * 100
            return progress