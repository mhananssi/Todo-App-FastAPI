from app.extensions import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class TodoItem(Base):
    __tablename__ = 'todoitems'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String, nullable=False)
    due_date = Column(DateTime)
    is_done = Column(Boolean, default=False)
    user = relationship('User')

    def __repr__(self):
        return "<User(id='{}', user_id='{}', title='{}', description='{}', due_date='{}', is_done='{}')>".format(
            self.id, self.user_id, self.title, self.description, self.due_date, self.is_done)
