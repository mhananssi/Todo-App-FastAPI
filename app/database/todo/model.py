from app.extensions import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey


class TodoItem(Base):
    __tablename__ = 'todoitems'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(String)
    datetime = Column(DateTime)
    is_done = Column(Boolean, default=False)

    def __repr__(self):
        return "<User(id='{}', user_id='{}', title='{}', description='{}', datetime='{}', is_done='{}')>".format(
            self.id, self.user_id, self.title, self.description, self.datetime, self.is_done)
