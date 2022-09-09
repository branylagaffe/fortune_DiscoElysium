
from turtle import color
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Conversations(Base):
    __tablename__ = 'conversations'

    id               = Column('id', BigInteger, primary_key=True)
    #conversationsID = Column('conversationsid', BigInteger)
    articy_id        = Column('articyId', Text)
    title            = Column('title', Text)
    description      = Column('description', Text)
    actor_id         = Column(Integer, ForeignKey('actors.id'))
    conversant_id    = Column(Integer, ForeignKey('actors.id'))

    actor_id_rel      = relationship("Actors", foreign_keys=[actor_id])
    conversant_id_rel = relationship("Actors", foreign_keys=[conversant_id])
