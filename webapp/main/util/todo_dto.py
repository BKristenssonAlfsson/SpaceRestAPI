from flask_restplus import Namespace, fields

class TodoDto:

    api = Namespace('todo', description="Todo list")

    todo = api.model('todo', {
        'id': fields.String(description="ID"),
        'todo': fields.String(description="What to do", required=True),
        'done': fields.Boolean(description="Done or not")
    })