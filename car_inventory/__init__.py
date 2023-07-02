from flask import Flask 
from flask_marshmallow import Marshmallow
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from .helpers import JSONEncoder
from .models import db as root_db, login_manager, ma
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
ma = Marshmallow(app)

import json

app = Flask(__name__)
app.json_encoder = json.JSONEncoder

# @app.route("/") #simple route on the homepage
# def hello_world():
#     return "<p>Hello, World!</p>"

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.config.from_object(Config)
root_db.init_app(app)
migrate = Migrate(app, root_db)
ma.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
app.json_encoder = JSONEncoder
CORS(app)
