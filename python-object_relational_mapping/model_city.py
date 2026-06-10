#!/usr/bin/python3
"""SQLAlchemy ORM model for the City class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Maps to the 'cities' table in MySQL.

    Attributes:
        id       (int): Auto-incremented primary key, never null.
        name     (str): City name, max 128 chars, never null.
        state_id (int): Foreign key referencing states.id, never null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
