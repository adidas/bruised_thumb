from sqlalchemy import (
    Column,
    Text,
    Date
)

from .meta import Base


class Post(Base):
    __tablename__ = 'posts'
    date = Column(Date, primary_key=True)
    title = Column(Text)
    body = Column(Text)