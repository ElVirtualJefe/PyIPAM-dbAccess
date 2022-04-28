#import app.stubs.ipAddress_pb2
from uuid import UUID
import app.stubs.ipAddress_pb2_grpc
from app.stubs import ipAddress_pb2
from app.models.ipAddress import ipAddressModel
import uuid
from app import sess as session

class IpAddressServiceServicer(app.stubs.ipAddress_pb2_grpc.IpAddressServiceServicer):
    
    def __init__(self):
        pass

    def GetIpAddressById(self, request, context):
        resIpAddress = ipAddress_pb2.ipAddress()
        ip = ipAddressModel()

        try:
            ip = session.query(ipAddressModel).filter_by(id=request.id).first()
            print('%s' % ip.id)
            print('%s' % ip.ipAddress)
        except:
            print("Error...")

        resIpAddress.id = ip.id.__str__()
        resIpAddress.ipAddress = ip.ipAddress
        resIpAddress.is_gateway = ip.is_gateway
        resIpAddress.description = ip.description

        return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)

    def GetIpAddressByName(self, request, context):
        pass

    def GetIpAddressBySubnet(self, request, context):
        pass

    def AddIpAddress(self, request, context):
        newIpAddress = ipAddress_pb2.ipAddress()
        print(f"Adding new IP Address...")
        newIpAddress.id = uuid.uuid4().__str__()
        newIpAddress.ipAddress = request.ipAddress
        print('ipAddress Description = %s' % request.description)
        print('ipAddress MAC Address = %s' % request.macAddress)
        print('ipAddress Description = %s' % request.description)

        return ipAddress_pb2.IpAddressResponse(ipAddress=newIpAddress)

