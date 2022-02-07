from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus as urlquote
from app.models import db

import os;
env = os.getenv('FLASK_ENV')

# App Config - the minimal footprint
#app.config.from_object("config.DevelopmentConfig")
#if (env == "development"):
#    config.from_object("config.DevelopmentConfig")
#else:
#    config.from_object("config.TestingConfig")

#config['TESTING'   ] = True 
#config['SECRET_KEY'] = 'S#perS3crEt_JamesBond' 

# our database uri
username = config.get("postgres","DB_USERNAME")
password = urlquote(config.get("postgres","DB_PASSWORD"))
dbname = config.get("postgres","DB_NAME")
dbserver = config.get("postgres","DB_SERVER")
dbport = config.getint("postgres","DB_PORT")

SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@{dbserver}:{dbport}/{dbname}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

import models

engine = create_engine(SQLALCHEMY_DATABASE_URI)
#Base.metadata.create_all(engine)
db.create_all(engine)

Session = sessionmaker(bind=engine)
sess = Session()


