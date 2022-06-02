from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import expression as exp
from sqlalchemy import Column,String,DateTime
from sqlalchemy import func,text
import uuid
from datetime import datetime
from . import Base

class settingsModel(Base):
    """
    Settings Model
    """

    __tablename__ = "settings"

    id = Column(UUID(True), primary_key=True, server_default=text('uuid_generate_v4()'))
    category = Column(String(24))
    name = Column(String(48))
    value = Column(String(120))
    dateLastEdited = Column(DateTime)
    dateCreated = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Setting - {self.name}: {self.value}>"
