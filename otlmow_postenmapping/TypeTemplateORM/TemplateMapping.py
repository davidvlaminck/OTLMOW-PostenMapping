from sqlalchemy import Column, String, Boolean, Integer

from otlmow_postenmapping.TypeTemplateORM.Base import Base


class TemplateMapping(Base):
    __tablename__ = 'MappingSB250'
    standaardpostnummer = Column(String, primary_key=True, nullable=False)
    typeURI = Column(String, nullable=False)
    attribuutURI = Column(String, nullable=False)
    dotnotatie = Column(String, nullable=False)
    defaultWaarde = Column(String)
    rijNummer = Column(Integer, primary_key=True, nullable=False)
    tempID = Column(String, nullable=False)
    isHoofdAsset = Column(Boolean, nullable=False)
