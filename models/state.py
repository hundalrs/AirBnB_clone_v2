#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
import os
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                            cascade="delete, all, delete-orphan")
    else:
        @property
        def cities(self):
            '''
                Getter for cities when using FileStorage system
            '''
            cls_dict = models.storage.all(City)
            cities_in_state = []
            current_state = State.id
            for key, value in cls_dict.items():
                if value.state_id == current_state:
                    cities_in_state.append(value)
            return cities_in_state
