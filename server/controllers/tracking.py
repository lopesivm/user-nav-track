import traceback

from flask.globals import request
from flask_restful import Resource

from services import tracking_service

class TrackingService(Resource):
    def post(self, uuid):
        try:
            input_json = request.get_json()
            if input_json:
                if not tracking_service.enqueue_post_track(uuid, input_json['title'],
                                                   input_json['url'], input_json['datetime']):
                    return {'error': 'Service temporarily unavailable'}, 503
            else:
                return {'error': 'No JSON data received'}, 400
        except Exception:
            return {'error': 'Internal fatal error occurred', 'traceback': traceback.format_exc()}, 500
        return {'message': 'success'}, 200

class EmailRegistryService(Resource):
    def post(self, uuid):
        try:
            input_json = request.get_json()
            if input_json:
                if not tracking_service.register_email(uuid, input_json['email']):
                    return {'error': 'Service temporarily unavailable'}, 503
            else:
                return {'error': 'No JSON data received'}, 400
        except Exception:
            return {'error': 'Internal fatal error occurred', 'traceback': traceback.format_exc()}, 500
        return {'message': 'success'}, 200