

from os import path
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base, classname_for_table
from sqlalchemy.orm import Session



DIR = path.dirname(path.realpath(__file__))
DB  = path.relpath(path.join(DIR, 'databases', 'sqlite', 'discobase12-17-2021-4-18-51-PM.db'), DIR)

engine = create_engine("sqlite:///{}".format(DB), echo=True, future=True)

Base = automap_base()
Base.prepare(autoload_with=engine)

Actors = Base.classes.actors
Dialogues = Base.classes.dialogues

session = Session(engine)

a_actor = session.query(Actors).first()
c = session.query(Dialogues).first()

print(c.description)