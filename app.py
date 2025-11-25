tasks = []

def add_task(title):
    if not title or not title.strip():
        raise ValueError("Title cannot be empty")
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    return task

def list_tasks():
    return list(tasks)

def update_task(task_id, completed=None, title=None):
    for task in tasks:
        if task["id"] == task_id:
            if title is not None:
                if not title or not title.strip():
                    raise ValueError("Title cannot be empty")
                task["title"] = title
            if completed is not None:
                task["completed"] = completed
            return task
    return None

def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False

def clear_tasks():
    tasks.clear()
