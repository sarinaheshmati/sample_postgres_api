import datetime
from cgitb import enable
from sqlite3 import Timestamp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, false, true

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    enable = Column(Boolean, nullable=False, default=true)
    status = Column (Boolean, nullable=False, default=false)

class Logs(Base):
    __tablename__ = 'Logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Users.id), nullable=False)
    action = Column(String, nullable=False)
    status = Column(Boolean, nullable=False)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>"\
                .format(self.title, self.author, self.pages, self.published)