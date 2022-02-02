from flask import Blueprint, Flask
from config import config_options

import dateutil.parser



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
    
    # function to format dates
    @app.template_filter('strftime')
    def _jinja2_filter_datetime(date, fmt=None):
        date = dateutil.parser.parse(date)
        native = date.replace(tzinfo=None)
        format='%b %d, %Y'
        return native.strftime(format) 
    
    return app

