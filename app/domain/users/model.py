from app.extensions import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    uname = Column(String)
    password_hash = Column(String)

    def __repr__(self):
        return "<User(id='{}', email='{}', uname={})>".format(self.id, self.email, self.uname)
