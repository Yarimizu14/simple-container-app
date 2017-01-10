from app import db
import datetime
import enum
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    Index
)


class Messages(db.Model):
    __tablename__ = 'messages'

    # nullable: default is True

    id = db.Column(Integer, primary_key=True)
    message = db.Column(String(), index=False, nullable=False)

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return '<id {}, message {}>'.format(
            self.id, self.message
        )

    def to_dict(self):
        return {'id': self.id, 'message': self.message}
