from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import Column,String,DateTime,SmallInteger
import uuid
from . import Base

class vLanModel(Base):
    """
    vLAN Model
    """

    __tablename__ = "vlans"

    id = Column(UUID(True), primary_key=True, default=uuid.uuid4)
    name = Column(String(48))
    vlanNumber = Column(SmallInteger)
    description = Column(String(250))
    subnets = relationship('subnetModel', backref='subnets', lazy=True)
    dateLastEdited = Column(DateTime)

    def __repr__(self):
        return f"<vLAN: {self.vlanNumber} - {self.name}>"
