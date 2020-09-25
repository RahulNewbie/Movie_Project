from flask import Flask
from utility import constants
from server.blueprint.api import api


app = Flask(__name__)
app.register_blueprint(api)


def run_server(db_obj):
    app.config['DB'] = db_obj
    app.run(host='0.0.0.0', port=constants.SERVICE_PORT)
