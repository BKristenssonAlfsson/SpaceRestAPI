from flask import request, Response
from ..model.nasa_model import Nasa
from .. import session
from ..util.nasa_dto import NasaDto
from flask_restplus import Resource
from ..queries import mysql_queries

api = NasaDto.api
nasa = NasaDto.nasa

@api.route('/')
class AllImages(Resource):
    @api.marshal_list_with(nasa)
    def get(self):
        images = session.query(Nasa).all()
        return images, 200

@api.route('/add')
class AddUser(Resource):
    @api.marshal_with(nasa)
    def post(self):
        dict_body = request.get_json()
        response_message = ""
        status_code = 503
        
        image_to_add = Nasa(copyright=dict_body['copyright'],
                            date=dict_body['date'],
                            explanation=dict_body['explanation'],
                            hdurl=dict_body['hdurl'],
                            media_type=dict_body['media_type'],
                            service_version=dict_body['service_version'],
                            title=dict_body['title'],
                            url=dict_body['url'])

        check = mysql_queries.check_title(dict_body['title'])

        if (check == "OK"):
            session.add(image_to_add)
            session.commit()
            session.close()
            response_message = "Image added"
            status_code = 201
        elif (check == "False"):
            response_message = "Image not added due to already in database"
            status_code = 409

        return (response_message), status_code