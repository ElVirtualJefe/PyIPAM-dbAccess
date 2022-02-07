from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column,String,DateTime
import uuid
from . import Base

class settingsModel(Base):
    """
    Settings Model
    """

    __tablename__ = "settings"

    id = Column(UUID(True), primary_key=True, default=uuid.uuid4)
    category = Column(String(24))
    name = Column(String(48))
    value = Column(String(120))
    dateLastEdited = Column(DateTime)

    def __repr__(self):
        return f"<Setting - {self.name}: {self.value}>"
