#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    meta = Base.metadata
    place_amenity = Table('place_amenity', meta, Column('place_id', String(60),
                          ForeignKey('places.id'), primary_key=True,
                          nullable=False),
                          Column('amenity_id', String(60),
                          ForeignKey('amenities.id'),
                          primary_key=True, nullable=False))

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary=Place.place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """
            reviews getter
            """
            instances = storage.all()
            reviews_list = []
            for i in instances:
                classname = i.__class__.__name__
                if i.place_id == self.id and classname == 'Review':
                    reviews_list.append(i)
            return reviews_list

        @property
        def amenities(self):
            """
            amenities getter"
            """
            instances = storage.all()
            amenitieslist = []
            for i in instances:
                classname = i.__class__.__name__
                if i.place_id == self.id and classname == 'Amenity':
                    amenitieslist.append(i)
            return (amenitieslist)

        @amenities.setter
        def amenities(self, obj):
            """
            amenities setter
            """
            if obj.__class__.__name__ == 'Amenity':
                amenity_ids.append(obj.id)
