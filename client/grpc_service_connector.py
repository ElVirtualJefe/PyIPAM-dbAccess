from configparser import ConfigParser
import grpc

config = ConfigParser()
config.read("config.ini")

class GrpcServiceConnector(object):
    
    def __init__(self,service_class):
        #server_address = config.get("server","ADDRESS")
        server_address = 'localhost'
        server_port = config.get("server","PORT")
        self._grpc_api_address = '%s:%s' % (server_address,server_port)
        self._channel = None
        self._stub = None
        self._service_class = service_class

    def start(self):
        self._channel = grpc.insecure_channel(self._grpc_api_address)
        self._stub = self._service_class(self._channel)

    @property
    def stub(self):
        if self._stub is None:
            service_class_name = self._service_class.__name__
            raise AttributeError("stub '%s' is empty" % service_class_name)

        #print(f"{self._stub}")
        return self._stub

