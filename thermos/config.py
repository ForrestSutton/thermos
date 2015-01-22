import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY= '\xb4\xdfj\xd8\n~\x9c\xbc]\xbd\x12S\x8a\xc5\xcb\x05_\xc0\xc4\xf0\xa5\xb0r\xaf'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///'+ os.path.join(basedir, 'thermos.db')

class TestingConfig(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI= 'sqlite:///'+ os.path.join(basedir, 'data-test.db')
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI= 'sqlite:///'+ os.path.join(basedir, 'thermos.db')

config_by_name = dict(
    dev = DevelopmentConfig,
    test = TestingConfig,
    prod = ProductionConfig
)
