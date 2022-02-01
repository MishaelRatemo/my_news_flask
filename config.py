# from distutils.command.config import config
# from distutils.debug import DEBUG
import os

# from instance.config import NEWS_API_KEY

class Config:
      NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    #   NEWS_API_BASE_URL = os.environ.get('NEWS_API_BASE_URL')
      
      
      NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
  
    #   SOURCES_URL= 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
      
      
class ProdConfig(Config):
    pass

class DeveConfig(Config):
    DEBUG= True
    
config_options ={
    'development' : DeveConfig,
    'production' : ProdConfig
}