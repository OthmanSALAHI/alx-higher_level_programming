#!/usr/bin/python3
"""prints the first state"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3066/{}".
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    nameCheck = argv[4]
    id_state = session.query(State).filter(State.name == nameCheck).first()
    print(f"{id_state.id}" if id_state else "Not found")
