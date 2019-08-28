from flask import request, Response
from .. import session
from ..util.nasa_dto import NasaDto
from flask_restplus import Resource


api = NasaDto.api
nasa = NasaDto.nasa

@api.route('/')
class AllImages(Resource):
    @api.marshal_list_with(nasa)
    def get(self):
        return 205