from sqlalchemy import Column
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer, ForeignKey
from config.db import Base

# Define the table
class Survey_Area(Base):
    __tablename__ = 'survey_areas'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    area_id:Mapped[int] = mapped_column(Integer, ForeignKey('areas.id'), nullable=False)
    survey_id:Mapped[int] = mapped_column(Integer, ForeignKey('surveys.id'), nullable=False)
    
    area = relationship('Area', back_populates='areas')
    survey = relationship('Survey', back_populates='surveys')
