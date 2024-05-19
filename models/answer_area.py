from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer, ForeignKey
from config.db import Base

# Define the table
class Answer_Area(Base):
    __tablename__ = 'answer_area'
    id = Mapped[int] = mapped_column(Integer, primary_key=True)
    area_id = Mapped[int] = mapped_column(Integer, ForeignKey('area.id'), nullable=False)
    survey_id = Mapped[int] = mapped_column(Integer, ForeignKey('survey.id'), nullable=False)
    
    area = relationship('Area', back_populates='areas')
    survey = relationship('survey', back_populates='answers')