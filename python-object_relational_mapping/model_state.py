#!/usr/bin/python3
"""SQLAlchemy ORM model for the State class.

Base is the registry SQLAlchemy uses to track all mapped classes and
their corresponding tables. Every model must inherit from the same Base
so that Base.metadata.create_all(engine) can discover and create all
tables in one call.

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()
class State(Base):
    """Maps to the 'states' table in MySQL.

    Attributes:
        id   (int): Auto-incremented primary key, never null.
        name (str): State name, max 128 chars, never null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
