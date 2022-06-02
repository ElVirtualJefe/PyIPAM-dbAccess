from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression as exp
from sqlalchemy import Column,String,DateTime,ForeignKey,Boolean
from sqlalchemy import func,text
import uuid
from datetime import datetime
from . import Base

class subnetModel(Base):
    """
    Subnet Model
    """

    # table name
    __tablename__ = 'subnets'

    id = Column(UUID(True), primary_key=True, server_default=text('uuid_generate_v4()'))
    name = Column(String(48))
    displayName = Column(String(128))
    ipAddresses = relationship('ipAddressModel', backref='ipAddresses', lazy=True)
    masterSubnet_id = Column(UUID(True), ForeignKey('subnets.id'), nullable=True)
    vlan_id = Column(UUID(True), ForeignKey('vlans.id'), nullable=True)
    allowRequests = Column(Boolean, server_default=exp.false(), nullable=False)
    dateLastEdited = Column(DateTime(timezone=True), onupdate=datetime.utcnow, server_default=func.now())
    dateLastScanned = Column(DateTime(timezone=True))
    dateLastDiscovered = Column(DateTime(timezone=True))
    dateCreated = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    doDiscovery = Column(Boolean, server_default=exp.false())
    doScan = Column(Boolean, server_default=exp.false())

    def __repr__(self):
        return f"<Subnet Name: {self.name}>"

