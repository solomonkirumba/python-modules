from datetime import datetime

def validate_task_title(title):
    if not title.strip():
        print("Error: Task title cannot be empty.")
    if title.isdigit():
        print("Error: Task title must contain letters.")
    if len(title) > 100:
        print("Error: Task title cannot exceed 100 characters.")
def validate_task_description(description):
    if not description.strip():
        print("Error: Task description cannot be empty.")
    if len(description) > 500:
        print("Error: Task description cannot exceed 500 characters.")
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Error: Due date must be in YYYY-MM-DD format.")
    if datetime.strptime(due_date, "%Y-%m-%d") < datetime.now():
        print("Error: Due date cannot be in the past.")
    if datetime.strptime(due_date, "%Y-%m-%d").month > 12 or datetime.strptime(due_date, "%Y-%m-%d").day > 31:
        print("Error: Invalid due date.")