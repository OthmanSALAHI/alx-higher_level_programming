#!/usr/bin/python3
"""Contains State class and Base and City"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in res:
        print(f"{state.name}: ({city.id}) {city.name}")
