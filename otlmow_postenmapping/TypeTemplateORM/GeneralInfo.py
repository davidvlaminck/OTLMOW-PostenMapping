from sqlalchemy import Column, String

from otlmow_postenmapping.TypeTemplateORM.Base import Base


class Info(Base):
    __tablename__ = 'GeneralInfo'
    parameter = Column(String, primary_key=True)
    waarde = Column(String)
