class Config(object):
    DEBUG  = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True