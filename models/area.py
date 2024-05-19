from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base

# Define the table
class Area(Base):
    _tablename_ = 'areas'
    id = Mapped[int] = mapped_column(Integer, primary_key=True)
    name = Mapped[str] = mapped_column(String(50), nullable=False)
