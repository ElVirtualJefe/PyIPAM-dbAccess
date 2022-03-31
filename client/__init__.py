from configparser import ConfigParser
#from typing import Text
#import grpc

config = ConfigParser()
config.read("config.ini")

from app.stubs import ipAddress_pb2,ipAddress_pb2_grpc
import grpc
from google.protobuf import text_format

class GrpcServiceConnector(object):

    def __init__(self,service_class):
        server_address = config.get("server","ADDRESS")
        server_port = config.get("server","PORT")
        self._grpc_api_address = '%s:%s' % (server_address,server_port)
        self._channel = None
        self._stub = None
        self._service_class = service_class

    def start(self):
        self._channel = grpc.insecure_channel(self._grpc_api_address)
        self._stub - self._service_class(self._channel)

    @property
    def stub(self):
        if self._stub is None:
            service_class_name = self._service_class.__name__
            raise AttributeError("stub '%s' is empty" % service_class_name)

        return self._stub

class TextClient(object):
    #
    def __init__(self):
        self.ipAddress_conn = GrpcServiceConnector(ipAddress_pb2_grpc.IpAddressServiceStub)
        #
        self.ipAddress_conn.start()
    #
    def get_ip_address_by_id(self,id):
        req = ipAddress_pb2.IpAddressIdRequest(id=id)
        res = self.ipAddress_conn.stub.GetIpAddressById(req)
        #return ipAddress_pb2.IpAddressResponse(res)
        return res

