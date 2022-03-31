#import app.stubs.ipAddress_pb2
import app.stubs.ipAddress_pb2_grpc
from client.stubs import ipAddress_pb2

class IpAddressServiceServicer(app.stubs.ipAddress_pb2_grpc.IpAddressServiceServicer):
    
    def __init__(self):
        pass

    def GetIpAddressById(self, request, context):

        return ipAddress_pb2.IpAddressResponse()

    def GetIpAddressByName(self, request, context):
        pass

    def GetIpAddressBySubnet(self, request, context):
        pass

