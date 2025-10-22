from decouple import config

class Config(object):
    SECRET_KEY = config('SECRET_KEY', default='your-secret-key')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

