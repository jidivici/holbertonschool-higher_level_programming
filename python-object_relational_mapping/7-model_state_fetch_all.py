#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa.

ORM mindset:
- create_engine() sets up the connection pool (no query yet)
- Session is the "workspace": all ORM operations go through it
- session.query(State).order_by(State.id) translates to:
      SELECT * FROM states ORDER BY id ASC
  but returns State objects instead of raw tuples
- We access .id and .name attributes instead of tuple indices
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
