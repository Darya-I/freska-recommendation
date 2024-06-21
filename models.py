# models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from config import DATABASE_URI

Base = declarative_base()
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

class UserCartItem(Base):
    __tablename__ = 'UserCartItem'
    Id = Column(Integer, primary_key=True)
    UserId = Column(String)
    ProductId = Column(Integer)
    Quantity = Column(Integer)
    AddedAt = Column(DateTime)
    
class UserPreference(Base):
    __tablename__ = 'UserPreference'
    Id = Column(Integer, primary_key=True)
    UserId = Column(String)
    CategoryId = Column(Integer)
    CreatedAt = Column(DateTime)

class UserSession(Base):
    __tablename__ = 'UserSession'
    Id = Column(Integer, primary_key=True)
    UserId = Column(String)
    StartTime = Column(DateTime)
    EndTime = Column(DateTime)
    SessionInfo = Column(String)
