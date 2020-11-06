#!/usr/bin/python3
"""
task 11
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """
    func
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print("{}".format(new.id))
    session.close()
