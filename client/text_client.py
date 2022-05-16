from stubs import ipAddress_pb2,ipAddress_pb2_grpc
from stubs import dbaccess_pb2,dbaccess_pb2_grpc
from grpc_service_connector import GrpcServiceConnector

class TextClient(object):
    
    def __init__(self):
        self.ipAddress_conn = GrpcServiceConnector(ipAddress_pb2_grpc.IpAddressServiceStub)        
        self.ipAddress_conn.start()

        self.dbAccess_conn = GrpcServiceConnector(dbaccess_pb2_grpc.DBAccessStub)
        self.dbAccess_conn.start()
    
    def get_ip_address_by_id(self,id):
        try:
            req = ipAddress_pb2.IpAddressIdRequest(id = id)
            res = self.ipAddress_conn.stub.GetIpAddressById(req)
        except Exception as e:
            print(e)
            return "[ERROR] Could not find a row with id %s" % id
        #return ipAddress_pb2.IpAddressResponse(res)
        #return res
        print("Exiting the function...")
        return res

    def add_new_ip_address(self,ip,is_gateway=False,description='',hostname='',mac='',owner=''):
        req = ipAddress_pb2.ipAddress(
            ipAddress = ip,
            is_gateway = is_gateway,
            description = description,
            hostname = hostname,
            macAddress = mac,
            owner = owner
        )
        res = self.ipAddress_conn.stub.AddIpAddress(req)
        return res

    def write_to_table(self,**columns):
        req = dbaccess_pb2.objIpAddress()
        res = self.dbAccess_conn.stub.writeIpAddress(req)
        return res

