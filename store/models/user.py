from sqlalchemy import Column, Integer, String, DateTime, Boolean

from store.engine.utils import utc_now
from store.models import Base, session


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    last_login = Column(DateTime, nullable=False, default=utc_now())
    created_on = Column(DateTime, default=utc_now())
    modified_on = Column(DateTime, onupdate=utc_now())

    def update_last_login(self, user_id):
        """
        Update a Last Login Time Whenever user login
        :param user_id: integer: unique id to identify particular user.
        :return: None
        """
        session.query(
            User
        ).filter(
            User.id == user_id,
            User.active == True
        ).update({'last_login': utc_now()})
        session.flush()

        return None  # Python returns None, but better do it explicitly.!!!
