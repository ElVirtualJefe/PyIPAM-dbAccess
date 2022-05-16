import sqlalchemy
from app.stubs import dbaccess_pb2, dbaccess_pb2_grpc as db_grpc
from app.models import Base,db
from app import sess as session

class DBAccessServicer(db_grpc.DBAccessServicer):
    
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
        return dbaccess_pb2.writeResponse()