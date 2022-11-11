from app.extensions import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    uname = Column(String)
    password_hash = Column(String)
    is_verified = Column(Boolean, default=False)

    def __repr__(self):
        return "<User(id='{}', email='{}', uname={}, is_verified={})>".format(self.id, self.email, self.uname,
                                                                              self.is_verified)
