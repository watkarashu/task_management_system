from .task import Task

def create_task(title,description,Category=None):
    new_task=Task(title,description,Category)
    return new_task