from flask_restplus import Namespace, fields

class TodoDto:

    api = Namespace('todo', description="Todo list")

    todo = api.model('todo', {
        'id': fields.String(description="ID"),
        'label': fields.String(description="What to do title", required=True),
        'description': fields.String(description="What is it all about", required=True),
        'done': fields.Boolean(description="Done or not")
    })