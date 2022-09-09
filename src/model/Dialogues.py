from turtle import color
from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Hold each line of dialogues, as well as the modifiers
# needed to pass passive check
class Dialogues(Base):
    __tablename__ = "dialogues"

    id              = Column('id', BigInteger, primary_key=True)
    dialogue_id     = Column('dialogueId', BigInteger)
    title           = Column('title', Text)
    text            = Column('text', Text)
    articy_id       = Column('articyId', Text)
    actor_id        = Column(Integer, ForeignKey('actors.id'))
    entryType       = Column('entryType', String)
    conversation_id = Column(BigInteger, ForeignKey('conversations.id'))
    voiceLine       = Column('voiceLine', Text)
