from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column,String
import uuid
from . import Base

class addressStateModel(Base):
    """
    Address State Model
    """

    __tablename__ = "addressStates"

    id = Column(UUID(True), primary_key=True, default=uuid.uuid4)
    state = Column(String(48))

    def __repr__(self):
        return f"<State: {self.state}>"
