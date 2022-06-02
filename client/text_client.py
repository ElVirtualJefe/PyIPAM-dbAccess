from multiprocessing.dummy import Array
from psycopg2 import DataError
from sqlalchemy import null
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
        newAddress = ipAddress_pb2.ipAddress(
            ipAddress = ip,
            is_gateway = is_gateway,
            description = description,
            hostname = hostname,
            macAddress = mac,
            owner = owner
        )
        req = dbaccess_pb2.writeMessage(
            tablename = 'ipAddresses',
            message = newAddress.SerializeToString()
        )
        res = self.dbAccess_conn.stub.writeRowToTable(req)
        return res

    def write_to_table(self,tableName,**columns):
        req = dbaccess_pb2.writeMessage()

        #tableName = columns['tableName']
        #print(tableName)

        #message = columns['columns']
        #print(columns)

        match tableName:
            case 'ipAddresses':
                newAddress = ipAddress_pb2.ipAddress(
                    ipAddress = columns.get('ip'),
                    subnet_id = columns.get('subnet_id'),
                    is_gateway = columns.get('is_gateway'),
                    description = columns.get('description'),
                    hostname = columns.get('hostname'),
                    macAddress = columns.get('mac'),
                    owner = columns.get('owner')
                )
                #print(newAddress.SerializeToString())
                req = dbaccess_pb2.writeMessage(
                    tablename = tableName,
                    message = newAddress.SerializeToString()
                )
                
                

        res = self.dbAccess_conn.stub.writeRowToTable(req)
        return res

    def read_from_table(self,tableName,**filters):
        #print(len(filters))
        print(filters)
        #filter = [dbaccess_pb2.readFilter()] * len(filters)
        filter = []
        #print(filter)

        #if len(filters) > 0:
        tmpFilter = dbaccess_pb2.readFilter()
        for key in filters.keys():
            #print(key)
            #filter.pop(dbaccess_pb2.readFilter())
            attr = filters.get(key,None)
            #print(attr)
            if attr == None:
                raise DataError
            setattr(tmpFilter,'columnName',key)
            setattr(tmpFilter,'filterValue',attr)

            # Need to set this up to work with other comparison operators
        
            setattr(tmpFilter,'filterOperation',dbaccess_pb2.filterOps.EQUALS)

            filter.append(tmpFilter)


        print(filter)
        req = dbaccess_pb2.readMessage(
            tablename = tableName,
            readFilter = filter
        )

        res = self.dbAccess_conn.stub.readRowFromTable(req)
        
        return res