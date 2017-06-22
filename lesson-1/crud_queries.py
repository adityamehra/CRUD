from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

first = session.query(Restaurant).first()

print "Testing READ -"
print first.id
print first.name
print ""

veggie_burgers = session.query(MenuItem).filter_by(name='Veggie Burger')

for veggie_burger in veggie_burgers:
    print veggie_burger.id
    print veggie_burger.price
    print veggie_burger.restaurant.name
    print ""

for veggie_burger in veggie_burgers:
    if veggie_burger.price != '$2.99':
        veggie_burger.price = '$2.99'
        session.add(veggie_burger)
        session.commit()

for veggie_burger in veggie_burgers:
    print veggie_burger.id
    print veggie_burger.price
    print veggie_burger.restaurant.name
    print ""

spinach_ice_cream = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()

session.delete(spinach_ice_cream)
session.commit()

print session.query(MenuItem).filter_by(name='Spinach Ice Cream').one().name
