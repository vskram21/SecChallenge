import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///test.db', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

# Creates the table with the available metadata


# Add entries into the DB
def createdefaultusers():
    session = conn()
    Base.metadata.create_all(engine)
    session.add_all([
        User(username='admin', password='admin'),
        User(username='user', password='user')
        ])
    print ("DB Init")
    session.commit()

def conn():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
