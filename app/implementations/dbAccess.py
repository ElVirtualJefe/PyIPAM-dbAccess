from warnings import filters
from sqlalchemy import DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import exc as sa_exc

from datetime import datetime

from app.models.ipAddress import ipAddressModel
from app.stubs import dbaccess_pb2 as db_pb, dbaccess_pb2_grpc as db_grpc
from app.stubs import ipAddress_pb2 as ip_pb
from app.models import Base
from app import sess as session
import uuid

from . import helpers

class DBAccessServicer(db_grpc.DBAccessServicer):
    __regex_UUID = r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
    
    def __init__(self):
        return

    def _writeToTable(self,tablename, **columns):

        table = Base.metadata.tables[tablename]
        print(type(table))
        print(table.columns)
        print(table.constraints)

        for c in table.columns:
            t = str(c).split('.')[1]
            print(t)

            print(c.nullable)
            print(c.default)
            print(c.server_default)

            if (c.nullable == False):
                if t in columns:
                    print('We can fill this column!!')
                elif (c.default == None) and (c.server_default == None):
                    print('Houston, we have a problem!!') 
                    raise ValueError
                else:
                    print('There is a default value, so we don''t need to fill this column...')
            else:
                print('We can leave this one blank...')
            
        
        '''         
        for t in Base:
            if hasattr(t, '__tablename__') and t.__tablename__ == tablename:
                table = t
        
        if table == None:
            raise "Cannot find table with name %s " % tablename
        '''

        return Base.metadata.tables[tablename]

    def writeIpAddress(self, request, context):
        self._writeToTable('ipAddresses',ipAddress='172.16.105.32')
        return db_pb.writeResponse()

    def writeRowToTable(self, request, context):
        tableName = request.tablename
        #print(tableName)
        #table = Base.metadata.tables[tableName]
        #print(f'table = {table}')

        '''
        match tableName:
            case 'ipAddresses':
                inputMessage = ip_pb.ipAddress()
                inputMessage.ParseFromString(request.message)

                resMessage = ip_pb.ipAddress()

                queryModel = ipAddressModel
                model = helpers.createModelFromProtobufMessage(tableName,ipAddressModel,inputMessage)
                print(model)
        '''
        dataTypes = helpers.getDataTypeFromTable(tableName)
        #print(dataTypes)
        #print(dataTypes['MessageType'])
        #print(dataTypes['MessageType']())

        inputMessage = dataTypes['MessageType']()
        #print(inputMessage)
        inputMessage.ParseFromString(request.message)
        #print(inputMessage)
        resMessage = dataTypes['MessageType']()
        queryModel = dataTypes['model']

        model = helpers.createModelFromProtobufMessage(tableName,queryModel,inputMessage)
        #print(model)

        try:
            #print(model)
            print('Session add:')
            print(session.add(model))
            print('Session commit:')
            print(session.commit())

            statusCode = 200
            statusMessage = 'SUCCESSFUL'

            print('Get the committed row...')
            print(model.id)
            resRow = session.query(queryModel).filter('id'==model.id).first()
            print('Commited row:')
            print(resRow)

            resMessage = helpers.convertDbRowToProtobufMessage(tableName,resRow,dataTypes['MessageType'])
            print(resMessage)

        except sa_exc.IntegrityError as e:
            session.rollback()
            statusCode = 402
            statusMessage = str(e)
        except Exception as e:
            print("[ERROR] - ")
            print(e.__class__)
            print(e.__class__.__name__)
            print(e)
            session.rollback()
            statusCode = 402
            statusMessage = str(e)
        

        return db_pb.writeResponse(returnMessage=resMessage.SerializeToString(),statusCode=statusCode,statusMessage=statusMessage)

    def readRowFromTable(self, request, context):
        import re
        from sqlalchemy_filters import apply_filters
        
        #print(request)
        tableName = request.tablename
        readFilters = request.readFilter

        print(readFilters)
        #print(type(readFilters))

        dataTypes = helpers.getDataTypeFromTable(tableName)
        #print(dataTypes)
        inputMessage = dataTypes['MessageType']()
        resMessage = dataTypes['MessageType']()
        queryModel = dataTypes['model']

        query = session.query(queryModel)
        print(query)

        for i in readFilters:
            key = getattr(i,'columnName')
            value = getattr(i,'filterValue')
            print(db_pb.filterOps.LIKE)

            match getattr(i,'filterOperation',db_pb.filterOps.EQUALS):
                case db_pb.filterOps.EQUALS:
                    op = '='
                case db_pb.filterOps.LIKE:
                    op = 'LIKE'

            #query = apply_filters(query,filters,do_auto_join=False)
            query_text = f'"{key}" {op} \'{value}\''
            print(query_text)
            query = query.filter(text(query_text))
            print(query)

        result = query.all()
        print('result:')
        print(result)

        resMessage = helpers.convertDbRowToProtobufMessage(tableName,result,dataTypes['MessageType'])
        print(resMessage)
        statusCode = 200
        statusMessage = 'SUCCESSFUL'

        returnMessage = db_pb.readResponse(returnMessage=resMessage.SerializeToString(),statusCode=statusCode,statusMessage=statusMessage)
        print(returnMessage)


        return returnMessage

