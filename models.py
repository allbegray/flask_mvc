from datetime import datetime

from sqlalchemy import *

from database import Base


class Board(Base):
    __tablename__ = 'board'
    id = Column(BIGINT, primary_key=True)
    title = Column(String(length=255), nullable=False)
    content = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    updated_at = Column(TIMESTAMP, default=datetime.utcnow(), onupdate=datetime.utcnow())

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Board %r>' % self.title
