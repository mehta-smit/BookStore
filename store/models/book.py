from sqlalchemy import Column, Integer, String, DateTime, text, Boolean

from store.models import Base, db
from store.models.user import User
from store.engine.utils import utc_now


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    publication = Column(String(200), nullable=False)
    author1 = Column(String(200), nullable=False)
    author2 = Column(String(200), nullable=True)
    year = Column(Integer, nullable=False)
    added_on = Column(DateTime, default=utc_now())
    modified_on = Column(DateTime, onupdate=utc_now())
    deleted = Column(Boolean, nullable=False, default=False)


class BookOccupy(Base):
    __tablename__ = "book_occupy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, db.ForeignKey(Book.id), nullable=False)
    user_id = Column(Integer, db.ForeignKey(User.id), nullable=False)
    returned = Column(Boolean, default=False, nullable=False)
    occupy_on = Column(DateTime, default=utc_now())
    returned_on = Column(DateTime, onupdate=utc_now())
