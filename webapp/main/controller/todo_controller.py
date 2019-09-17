from ..model.todo_model import Todo
from flask_restplus import Resource
from flask import request, Response
from ..util.todo_dto import TodoDto
from ..queries import mongo_queries
from ..requests.to_rabbit import NasaRequests

api = TodoDto.api
todo = TodoDto.todo

check = NasaRequests.start

@api.route('/')
class AllTodos(Resource):
    @api.marshal_list_with(todo)
    def get(self):
        check()
        todos = []

        undone = mongo_queries.filter_for_undone_todos()

        for todo in undone:
            todos.append(todo)

        return todos, 200

@api.route('/add')
class AddTodo(Resource):
    @api.marshal_list_with(todo)
    def post(self):

        dict_body = request.get_json()
        print(dict_body)
        new_todo = Todo()

        todo_to_add = Todo(label=dict_body.get('label', ''),
                           description=dict_body.get('description', ''),
                           done=False)
                    

        new_todo = todo_to_add

        new_todo.save()

        return "OK", 202