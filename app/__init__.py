#print('__name__ = %s' % (__name__))

from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
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

#import app.models

engine = create_engine(SQLALCHEMY_DATABASE_URI)
#Base.metadata.create_all(engine)
db.create_all(engine)

Session = scoped_session(sessionmaker(bind=engine))
sess = Session()

import grpc,time
from concurrent import futures
from app.implementations import IpAddressServiceServicer
from app.stubs import ipAddress_pb2_grpc

_ONE_DAY_IN_SECONDS = 24 * 60 * 60

def serve():
    """Start grpc server servicing FMS RPCs."""
    print("Starting gRPC Server...")
    # create grpc server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # add services
    #health_servicer = HealthServicer()
    #item_master_servicer = ItemMasterServicer()
    ipAddressServicer = IpAddressServiceServicer()
    ipAddress_pb2_grpc.add_IpAddressServiceServicer_to_server(ipAddressServicer,server)

    # start server
    server_port = config.get("server","PORT")
    server_address = config.get("server","ADDRESS")
    address = '%s:%s' % (server_address, server_port)
    #logging.info('Starting grpc server at %s', address)

    server.add_insecure_port(address)
    server.start()
    print('gRPC Server running at %s' % address)

    # start() does not block so sleep-loop
    try:
        server.wait_for_termination()
        #while True:
            #time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        print("Stopping gRPC Server...")
        server.stop(0)

if __name__ == "app":
    print("Entering main program...")
    serve()
