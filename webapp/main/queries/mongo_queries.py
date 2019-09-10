from ..model.todo_model import Todo

def filter_for_undone_todos():
    undone = Todo.objects(done=False)
    
    return undone