#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''

    __tablename__ = 'place'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        reviews = relationship("Review", backref="place", cascade="delete")

    else:
        @property
        def reviews(self):
            '''
                Getter for getting all the reviews for the place
            '''
            cls_dict = models.storage.all(models.classes["Review"])
            reviews_of_place = []
            current_place = self.id
            for key, value in cls_dict.items():
                if value.place_id == current_place:
                    reviews_of_place.append(value)
            return reviews_of_place
