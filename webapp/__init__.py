    
from flask import Blueprint
from flask_restplus import Api
from flask_cors import CORS

from .main.controller.nasa_controller import api as nasa
from .main.controller.todo_controller import api as todo

blueprint = Blueprint('api', __name__, url_prefix='/api')
CORS(blueprint, support_credentials=True)

api = Api(blueprint,
          title="Space Data Service",
          description='Keeping data from different space agencies centralized')



'# Add more namespaces for other paths here'
api.add_namespace(nasa, path='/nasa')
api.add_namespace(todo, path='/todo')