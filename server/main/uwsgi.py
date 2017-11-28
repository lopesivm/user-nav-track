from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import config
import models
import utils

app = Flask(__name__, static_folder='../static', template_folder='../templates' )
api = Api(app)
cors = CORS(app, resources={r'/*': {'origins': '*'}})

def main():
    from controllers import admin_panel
    from controllers.tracking import TrackingService, EmailRegistryService

    api.add_resource(TrackingService, '/user/<uuid>/track')
    api.add_resource(EmailRegistryService, '/user/<uuid>/email')
    app.register_blueprint(admin_panel.blueprint)
    app.jinja_env.filters['last_access'] = utils.get_user_last_access
    app.jinja_env.filters['time_format'] = utils.print_datetime

models.init_engine(config.DB_PATH, pool_recycle=1)

main()