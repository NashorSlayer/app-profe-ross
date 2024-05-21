from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer, ForeignKey
from config.db import Base

# Define the table
class Answer_Area(Base):
    __tablename__ = 'answer_areas'
    id = Mapped[int] = mapped_column(Integer, primary_key=True)
    area_id = Mapped[int] = mapped_column(Integer, ForeignKey('areas.id'), nullable=False)
    survey_id = Mapped[int] = mapped_column(Integer, ForeignKey('surveys.id'), nullable=False)
    
    area = relationship('Area', back_populates='areas')
    survey = relationship('survey', back_populates='answers')