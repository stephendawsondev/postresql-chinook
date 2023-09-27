import os
from dotenv import load_dotenv

from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, Float
  )

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"

db = create_engine(db_url)

base = declarative_base()

# create the Artist class
class Artist(base):
  __tablename__ = "Artist"
  ArtistId = Column(Integer, primary_key=True)
  Name = Column(String)

class Album(base):
  __tablename__ = "Album"
  AlbumId = Column(Integer, primary_key=True)
  Title = Column(String)
  ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# Track table class
class Track(base):
  __tablename__ = "Track"
  TrackId = Column(Integer, primary_key=True)
  Name = Column(String)
  AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
  MediaTypeId = Column(Integer, primary_key=False)
  GenreId = Column(Integer, primary_key=False)
  Composer = Column(String)
  Milliseconds = Column(Integer, primary_key=False)
  Bytes = Column(Integer, primary_key=False)
  UnitPrice = Column(Float)


# create a session maker bound to our db
Session = sessionmaker(db)

# create a session
session = Session()

# create the db using the declarative base class
base.metadata.create_all(db)



# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist).all()
# for artist in artists:
#   print(artist.ArtistId, artist.Name, sep=" | ")


# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist).all()
# for artist in artists:
#   print(artist.Name, sep=" | ")

# Query 3 - Find Queen using name
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.Name)

# Query 4 - Find by artist id
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.Name)

# Query 5 - Select only artist ID from the Album table
# albums = session.query(Artist).filter_by(ArtistId=51).all()
# for album in albums:
#    print(album.Name)

# Query 6 - Find all tracks where the composer is Queen
tracks = session.query(Track).filter_by(Composer="Queen").all()
for track in tracks:
  print(
    track.TrackId, 
    track.Name, 
    track.AlbumId, 
    track.MediaTypeId, 
    track.GenreId, 
    track.Composer, 
    track.Milliseconds, 
    track.Bytes, 
    track.UnitPrice, 
    sep=" | "
    )