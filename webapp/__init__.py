    
from flask import Blueprint
from flask_restplus import Api
from flask_cors import CORS

blueprint = Blueprint('api', __name__, url_prefix='/api')
CORS(blueprint)

api = Api(blueprint,
          title="Space Data Service",
          description='Keeping data from different space agencies centralized')

'# Add more namespaces for other paths here'
#api.add_namespace(user, path='/user')