from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Actors(Base):
    __tablename__ = 'actors'

    id       = Column('id', BigInteger, primary_key=True)
    name     = Column('name', Text)
    isNPC    = Column('isNPC', Boolean)
    isPlayer = Column('isPlayer', Integer)
    color    = Column('color', Integer)

    dialogues = relationship('Dialogues')
    conversations = relationship('Conversations')