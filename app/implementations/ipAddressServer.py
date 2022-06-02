from uuid import UUID

import psycopg2.errors as err
from sqlalchemy import exc as sa_exc
from app.models import ipAddress
#import sqlalchemy

import app.stubs.ipAddress_pb2_grpc
from app.stubs import ipAddress_pb2
from app.models.ipAddress import ipAddressModel
import grpc
import uuid
from traceback import print_exc
from app import sess as session



class IpAddressServiceServicer(app.stubs.ipAddress_pb2_grpc.IpAddressServiceServicer):
    
    def __init__(self):
        return

    def _getIpAddress(self,request,context,search_type):
        resIpAddress = ipAddress_pb2.ipAddress()
        #ip = ipAddressModel()

        try:
            match search_type:
                case 'id':
                    print("Searching for IP Address with ID: %s..." % request.id)
                    ip = session.query(ipAddressModel).filter_by(id=request.id).first()
                    if (ip == None):
                        raise err.NoDataFound
                    else: 
                        print("Found %s with id %s" % (ip.ipAddress,request.id))
                case 'name':
                    pass
                case 'subnet':
                    pass
        except sa_exc.DataError as e:
            print("[ERROR] Invalid ID input: %s" % request.id)
            #print(e.args)
            #print_exc()
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("[ERROR] Invalid ID input: %s" % request.id)
            session.rollback()
            #return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)
        except err.NoDataFound as e:
            print("[ERROR] Could not find entry with id %s" % request.id)
            #print(e)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("[ERROR] Could not find entry with id %s" % request.id)
            session.rollback()
            #return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)
        except Exception as e:
            print("[ERROR] - ")
            print(e.__class__)
            print(e.__class__.__name__)
            print(e)
            session.rollback()
            #return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)
        else:
            #print(type(ip.id))
            resIpAddress.id = ip.id.__str__()
            resIpAddress.ipAddress = ip.ipAddress
            resIpAddress.is_gateway = ip.is_gateway
            resIpAddress.description = ip.description

        return resIpAddress

    def GetIpAddressById(self, request, context):
        resIpAddress = ipAddress_pb2.ipAddress()
        #ip = ipAddressModel()
        resIpAddress = self._getIpAddress(request,context,'id')

        ''' 
        try:
            print("Searching for %s..." % request.id)
            ip = session.query(ipAddressModel).filter_by(id=request.id).first()
            if (ip == None):
                raise err.NoDataFound
            else: 
                print("Found %s with id %s" % (ip.ipAddress,request.id))
        except sa_exc.DataError as e:
            print("[ERROR] Invalid ID input: %s" % request.id)
            #print(e.args)
            #print_exc()
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("[ERROR] Invalid ID input: %s" % request.id)
            session.rollback()
            #return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)
        except err.NoDataFound as e:
            print("[ERROR] Could not find entry with id %s" % request.id)
            #print(e)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("[ERROR] Could not find entry with id %s" % request.id)
            session.rollback()
            #return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)
        except Exception as e:
            print("[ERROR] - ")
            print(e.__class__)
            print(e.__class__.__name__)
            print(e)
            session.rollback()
            #return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)
        else:

            resIpAddress.id = ip.id.__str__()
            resIpAddress.ipAddress = ip.ipAddress
            resIpAddress.is_gateway = ip.is_gateway
            resIpAddress.description = ip.description
        '''

        return ipAddress_pb2.IpAddressResponse(ipAddress=resIpAddress)


    def GetIpAddressByName(self, request, context):
        pass


    def GetIpAddressBySubnet(self, request, context):
        pass


    def AddIpAddress(self, request, context):
        newIpAddress = ipAddress_pb2.ipAddress()
        print(f"Adding new IP Address...")
        #newIpAddress.id = uuid.uuid4().__str__()
        newIpAddress.ipAddress = request.ipAddress
        print('ipAddress Description = %s' % request.description)
        print('ipAddress MAC Address = %s' % request.macAddress)
        print('ipAddress Description = %s' % request.description)

        return ipAddress_pb2.IpAddressResponse(ipAddress=newIpAddress)

