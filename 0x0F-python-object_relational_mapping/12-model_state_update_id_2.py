#!/usr/bin/python3
"""
task 12
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == '2').first()
    state.name = "New Mexico"
    session.commit()
