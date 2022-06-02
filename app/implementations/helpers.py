from app.models import Base
from sqlalchemy import exc as sa_exc
from app.stubs import ipAddress_pb2 as ip_pb
from app.models.ipAddress import ipAddressModel


def getDataTypeFromTable(tableName):
    dataType = {}
    #table = Base.metadata.tables[tableName]
    #print(tableName)

    match tableName:
        case 'ipAddresses':
            dataType['MessageType'] = ip_pb.ipAddress
            
            #resMessage = ip_pb.ipAddress()

            dataType['model'] = ipAddressModel
            
    #print(dataType)

    return dataType

def convertDbRowToProtobufMessage(tableName,row,msgType):
    from sqlalchemy import DateTime
    from sqlalchemy.dialects.postgresql import UUID

    print(tableName)

    table = Base.metadata.tables[tableName]
    resMessage = msgType()

    print(row)

    for c in table.columns:
        print(c.name)
        attr = getattr(row,c.name,None)
        
        if attr == None:
            continue
        #print(type(c.type))
        if type(c.type) is UUID:
            attr = attr.__str__()
        elif type(c.type) is DateTime:
            attr = attr.__str__()
        
        print('attr:')
        print(attr)
        #print(type(attr))
        setattr(resMessage,c.name,attr)

    return resMessage


def createModelFromProtobufMessage(tableName,modelType,inputMessage):
    from app.stubs import dbaccess_pb2 as db_pb
    from sqlalchemy.dialects.postgresql import UUID

    import uuid

    table = Base.metadata.tables[tableName]
    model = modelType()
    
    #print(type(inputMessage))
    #print(inputMessage)
    #print("ListFields: ")
    #print(inputMessage.ListFields())
    #print(inputMessage.ListFields()[0][0].name)
    inputs = inputMessage.ListFields()

    for c in table.columns:
        t = c.name
        #print(t)
        #print(c.name)
        #print(type(c.type))
        #print(type(UUID))
        #attr = type(c.type)()
        #print(type(attr))

        if (c.nullable == False):
            print(t + " column is not nullable...")
            items = (item[0].name for item in inputs)
            if t in items:
                print('We can fill this column!!')
                #vars()[t] = getattr(inputMessage,t)
                #print(vars()[t])
                attr = getattr(inputMessage,t)
                #print(type(attr))
                if type(c.type) is UUID:
                    print('It is a UUID')
                    from psycopg2.extras import register_uuid
                    register_uuid()
                    attr = uuid.UUID(attr)
                #print(t + ':')
                #print(attr)
                #print(type(attr))
                #print(type(uuid.uuid4()))
                #print(type(getattr(model,t)))
                setattr(model,t,attr)
                #print(getattr(model,t))
                #print(type(getattr(model,t)))
            elif (c.default == None) and (c.server_default == None):
                print('Houston, we have a problem!!') 
                statusMessage = 'Value missing for column: ' + t
                raise sa_exc.DataError(statusMessage)
                #return db_pb.writeResponse(statusCode=401,statusMessage=statusMessage)
            else:
                print('There is a default value, so we don''t need to fill this column...')
                if type(c.type) is UUID and t == 'id':
                    print('It is the UUID for the ID column')
                    from psycopg2.extras import register_uuid
                    register_uuid()
                    #print(c.ColumnDefault)
                    #attr = UUID(attr)
                    #attr = adapt(uuid.UUID(attr)).getquoted()
                    setattr(model,t,uuid.uuid4())

        else:
            print('We can leave this one blank...')

    return model
        


