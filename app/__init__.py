from flask import Blueprint, Flask
from config import config_options

def  create_app(config_name):
    app = Flask(__name__)
    
    #app configuration
    app.config.from_object(config_options[config_name])
    
    # Blueprint registration 
    from .main import  root as app_blueprint
    app.register_blueprint(app_blueprint)
    
    # configuration setting
    from .requests import config_request
    config_request(app)
    
    return app