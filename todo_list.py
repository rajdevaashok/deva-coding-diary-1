# Simple To-Do List
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

add_task("Complete Git commit")
add_task("Review Python script")
print("Current Tasks:", tasks)
git add .
git commit -m "Added a simple to-do list script"
git push origin main
