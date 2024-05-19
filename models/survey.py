from sqlalchemy.orm import relationship,Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer, String, ForeignKey
from config.db import Base

# Define the table
class Survey(Base):
    __tablename__ = 'survey'
    id = Mapped[int] = mapped_column(Integer, primary_key=True)
    name = Mapped[str] = mapped_column(String(50), nullable=False)
    description = Mapped[str] = mapped_column(String(255), nullable=False)
    time_range_start = Mapped[int] = mapped_column(Integer(50), nullable=False)
    time_range_end = Mapped[int] = mapped_column(Integer(50), nullable=False)
    time_answer_start = Mapped[int] = mapped_column(Integer(50), nullable=False)
    time_answer_end = Mapped[int] = mapped_column(Integer(50), nullable=False)
    user_id = Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates='users')
    
