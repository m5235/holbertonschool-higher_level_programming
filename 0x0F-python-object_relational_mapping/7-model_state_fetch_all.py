#!/usr/bin/python3
"""
task7
"""

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session

if __name__ == "__main__":
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
    for e in session.query(State).order_by(State.id):
        print("{}: {}".format(e.id, e.name))
