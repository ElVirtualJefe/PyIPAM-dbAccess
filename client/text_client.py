from stubs import ipAddress_pb2,ipAddress_pb2_grpc
from grpc_service_connector import GrpcServiceConnector

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

