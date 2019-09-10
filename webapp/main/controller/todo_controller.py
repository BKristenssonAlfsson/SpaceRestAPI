from ..model.todo_model import Todo
from flask_restplus import Resource
from flask import request, Response
from ..util.todo_dto import TodoDto
from ..queries import mongo_queries

api = TodoDto.api
todo = TodoDto.todo

@api.route('/')
class AllTodos(Resource):
    @api.marshal_list_with(todo)
    def get(self):
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
        new_todo = Todo()

        todo_to_add = Todo(todo=dict_body.get('todo', ''),
                           done=dict_body.get('done', ''))
                    

        new_todo = todo_to_add

        new_todo.save()

        return "OK", 202