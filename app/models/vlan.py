from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression as exp
from sqlalchemy import Column,String,DateTime,SmallInteger
from sqlalchemy import func,text
import uuid
from datetime import datetime
from . import Base

class vLanModel(Base):
    """
    vLAN Model
    """

    __tablename__ = "vlans"

    id = Column(UUID(True), primary_key=True, server_default=text('uuid_generate_v4()'))
    name = Column(String(48))
    vlanNumber = Column(SmallInteger)
    description = Column(String(250))
    subnets = relationship('subnetModel', backref='subnets', lazy=True)
    dateLastEdited = Column(DateTime)
    dateCreated = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<vLAN: {self.vlanNumber} - {self.name}>"
