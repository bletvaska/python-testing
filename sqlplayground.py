from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine


URI = "sqlite:///chinook.sqlite"
engine = create_engine(URI)

Base = automap_base()
Base.prepare(engine, reflect=True)

Album = Base.classes.Album
Artist = Base.classes.Artist
Track = Base.classes.Track

from sqlalchemy.orm import Session
session = Session(engine)