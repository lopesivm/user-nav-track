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

    if __name__ == '__main__':
        from tornado.wsgi import WSGIContainer
        from tornado.httpserver import HTTPServer
        from tornado.ioloop import IOLoop

        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(5000)
        IOLoop.instance().start()

models.init_engine(config.DB_PATH, echo=False)

def test_dataset():
    from uuid import uuid4
    from datetime import datetime

    page_yahoo = models.Page(title='Yahoo', url='yahoo.com')
    page_steam = models.Page(title='Steam', url='steam.com')
    page_google = models.Page(title='Google', url='Google.com')

    user_ivan = models.User(uuid=str(uuid4()), email='ivanvlopes@gmail.com')
    user_julia = models.User(uuid=str(uuid4()), email='ju_kb@hotmail.com')

    # 2 Julia Yahoo Access
    access_julia_yahoo = models.Access(local_time=datetime.now(), server_time=datetime.now())
    user_julia.accesses.append(access_julia_yahoo)
    page_yahoo.accesses.append(access_julia_yahoo)
    access_julia_yahoo = models.Access(local_time=datetime.now(), server_time=datetime.now())
    user_julia.accesses.append(access_julia_yahoo)
    page_yahoo.accesses.append(access_julia_yahoo)

    # 1 Julia Google Access
    access_julia_google = models.Access(local_time=datetime.now(), server_time=datetime.now())
    user_julia.accesses.append(access_julia_google)
    page_google.accesses.append(access_julia_google)

    # 3 Ivan Steam Access
    access_ivan_steam = models.Access(local_time=datetime.now(), server_time=datetime.now())
    user_ivan.accesses.append(access_ivan_steam)
    page_steam.accesses.append(access_ivan_steam)
    access_ivan_steam = models.Access(local_time=datetime.now(), server_time=datetime.now())
    user_ivan.accesses.append(access_ivan_steam)
    page_steam.accesses.append(access_ivan_steam)
    access_ivan_steam = models.Access(local_time=datetime.now(), server_time=datetime.now())
    user_ivan.accesses.append(access_ivan_steam)
    page_steam.accesses.append(access_ivan_steam)

    # 2 Ivan Google Access
    access_ivan_google = models.Access(local_time=datetime.now(), server_time=datetime.now())
    user_ivan.accesses.append(access_ivan_google)
    page_google.accesses.append(access_ivan_google)
    access_ivan_google = models.Access(local_time=datetime.now(), server_time=datetime.now())
    user_ivan.accesses.append(access_ivan_google)
    page_google.accesses.append(access_ivan_google)

    session = models.get_session()
    session.add(user_ivan)
    session.add(user_julia)
    session.commit()

    # Total Google: 3
    # Total Yahoo: 2
    # Total Steam: 3

# test_dataset()

main()