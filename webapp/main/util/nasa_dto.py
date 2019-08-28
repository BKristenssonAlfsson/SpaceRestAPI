from flask_restplus import Namespace, fields

class NasaDto:
    
    api = Namespace('nasa', description="Nasa Data")

    nasa = api.model('nasa', {
        'id': fields.Integer(description="ID. Auto incremented"),
        'date': fields.Date(description='Date'),
        'explanation': fields.String(required=True, description="The image explanation"),
        'hdurl': fields.String(description="URL to HD image"),
        'media_type': fields.String(required=True, description="If it is Video or Image"),
        'service_version': fields.String(required=True, description="Which version the object has"),
        'title': fields.String(required=True, description="The objects title"),
        'url': fields.String(description="URL to image / video"),
        'copyright': fields.String(description="Author of the image")
    })