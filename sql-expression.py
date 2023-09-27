import os
from dotenv import load_dotenv

load_dotenv()

from sqlalchemy import (
  create_engine, MetaData, Table, Column, Integer, String, ForeignKey
  )

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"

# execute the instructions from our chinook local db
db = create_engine(db_url)

meta = MetaData(db)

# create a variable for the artist table
artist_table = Table("Artist", meta,
                     Column("ArtistId", Integer, primary_key=True),
                     Column("Name", String)
                     )

# create a variable for the album table
album_table = Table("Album", meta,
                    Column("AlbumId", Integer, primary_key=True),
                    Column("Title", String),
                    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
                    )

# create a variable for the track table
track_table = Table("Track", meta,
                    Column("TrackId", Integer, primary_key=True),
                    Column("Name", String),
                    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
                    Column("MediaTypeId", Integer, primary_key=False),
                    Column("GenreId", Integer, primary_key=False),
                    Column("Composer", String),
                    Column("Milliseconds", Integer),
                    Column("Bytes", Integer),
                    Column("UnitPrice", Integer)
                    )

with db.connect() as connection:
  # Query 1 - select all records from the "Artist" table 
  # select_query = artist_table.select()
  
  # Query 2 - select only the "Name" column from the "Artist" table
  # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

  # Query 3 - Find Queen using name
  # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

  # Query 4 - Find by artist id
  # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

  # Query 5 - Select only artist ID from the Album table
  # select_query = album_table.select().where(album_table.c.ArtistId == 51)

  # Query 6 - Find all tracks where the composer is Queen
  select_query = track_table.select().where(track_table.c.Composer == "Queen")

  results = connection.execute(select_query)

  for result in results:
    print(result)
