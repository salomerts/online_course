from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username  = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role  = Column(String)
    