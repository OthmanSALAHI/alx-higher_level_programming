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
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    def modify_state_name(state_id, new_name):
        # Query the state by ID
        state_to_modify = session.query(State).filter_by(id=state_id).first()

        if state_to_modify:
            state_to_modify.name = new_name
            session.commit()
            print(f"Modified state with ID {state_id} to {new_name}")
        else:
            print(f"State with ID {state_id} not found")
    modify_state_name(2, 'New Mexico')
