#import app.stubs.ipAddress_pb2
import app.stubs.ipAddress_pb2_grpc
from app.stubs import ipAddress_pb2

class IpAddressServiceServicer(app.stubs.ipAddress_pb2_grpc.IpAddressServiceServicer):
    
    def __init__(self):
        pass

    def GetIpAddressById(self, request, context):
        resIpAddress = ipAddress_pb2.ipAddress()

        
        resIpAddress.id = request.id
        resIpAddress.ipAddress = 'This is a miracle'


        return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)

    def GetIpAddressByName(self, request, context):
        pass

    def GetIpAddressBySubnet(self, request, context):
        pass

