from turtle import color
from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Links(Base):
    __tablename__ = "links"

    id                   = Column('id', BigInteger, primary_key=True)
    originDialogue       = Column('originDialogue', BigInteger)
    destinationDialogue  = Column('destinationDialogue', BigInteger)
    isConnector          = Column('isConnector', Boolean)
    conversationId       = Column('conversationId', BigInteger)
    outputConversationId = Column('outputConversationId', BigInteger)
    originIndex          = Column(BigInteger, ForeignKey('dialogues.id'))
