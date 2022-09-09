

from os import path
from sqlalchemy import create_engine



DIR = path.dirname(path.realpath(__file__))
DB = path.join(DIR, 'databases', 'sqlite', 'disco.sqlite3')

engine = create_engine("sqlite://{}".format(DB), echo=True, future=True)
