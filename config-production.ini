

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

    DB_NAME = "PyIPAM"
    DB_USERNAME = "postgres"
    DB_PASSWORD = "PyIPAM-P@ssw0rd123!"
    DB_PORT = 5432

    SESSION_COOKIE_SECURE = True

class ProductionConfig(Config):
    DB_SERVER = "pyipam-postgres"

class DevelopmentConfig(Config):
    DEBUG = True
    DB_SERVER = "pyipam-postgres"

class TestingConfig(Config):
    TESTING = True
    DB_SERVER = "localhost"
