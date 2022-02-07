from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import Column,String,DateTime,ForeignKey,Boolean
import uuid
from . import Base

class subnetModel(Base):
    """
    Subnet Model
    """

    # table name
    __tablename__ = 'subnets'

    id = Column(UUID(True), primary_key=True, default=uuid.uuid4)
    name = Column(String(48))
    ipAddresses = relationship('ipAddressModel', backref='ipAddresses', lazy=True)
    masterSubnet_id = Column(UUID(True), ForeignKey('subnets.id'), nullable=True)
    vlan_id = Column(UUID(True), ForeignKey('vlans.id'), nullable=True)
    allowRequests = Column(Boolean, default=False, nullable=False)
    dateLastEdited = Column(DateTime)
    dateLastScanned = Column(DateTime)
    dateLastDiscovered = Column(DateTime)
    doDiscovery = Column(Boolean)
    doScan = Column(Boolean)

    def __repr__(self):
        return f"<Subnet Name: {self.name}>"

