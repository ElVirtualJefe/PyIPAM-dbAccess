from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column,String,BigInteger,ForeignKey,Boolean,DateTime
import uuid
from . import Base

class ipAddressModel(Base):
    """
    IP Address Model
    """

    # table name
    __tablename__ = 'ipAddresses'

    id = Column(UUID(True), primary_key=True, default=uuid.uuid4)
    subnet_id = Column(UUID(True), ForeignKey('subnets.id'), nullable=False)
    ipAddress = Column(BigInteger, unique=True, index=True, nullable=False)
    is_gateway = Column(Boolean, default=False, nullable=False)
    description = Column(String(200))
    hostname = Column(String(64))
    macAddress = Column(String(17))
    owner = Column(String(40))
    state_id = Column(UUID(True), ForeignKey('addressStates.id'), nullable=False, default='5a3be258-876b-4fb3-9788-61acced67be1')
    dateLastSeen = Column(DateTime)
    dateLastEdited = Column(DateTime)

    def __repr__(self):
        return f"<id {id}>"

