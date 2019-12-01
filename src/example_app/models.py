from sqlalchemy import Column, Integer

from core.db import Base


class ExampleModel(Base):
    __tablename__ = "example"

    id = Column(Integer, primary_key=True)
