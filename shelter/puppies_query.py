from sqlalchemy import create_engine, extract
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

puppies = session.query(Puppy).order_by(Puppy.name)

for i, puppy in enumerate(puppies):
    print i + 1, puppy.name

puppies = session.query(Puppy).order_by(Puppy.weight)

for i, puppy in enumerate(puppies):
    print i+1, puppy.name, puppy.weight

puppies = session.query(Puppy).filter(((datetime.date.today().year - extract('year', Puppy.dateOfBirth)) * 12) + (datetime.date.today().month - extract('month', Puppy.dateOfBirth)) < 6 ).order_by(Puppy.dateOfBirth)

for i, puppy in enumerate(puppies):
    print i+1, puppy.name, puppy.weight, puppy.dateOfBirth

puppies = session.query(Puppy).group_by(Puppy.shelter_id)

for i, puppy in enumerate(puppies):
    print i+1, puppy.name, puppy.weight, puppy.shelter_id
