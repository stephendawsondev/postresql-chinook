import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


# Connect to an existing database
connection = psycopg2.connect(
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

# Add a cursor
cursor = connection.cursor()

# Execute a command that gets all Artists
# cursor.execute('SELECT * FROM "Artist";')

# cursor.execute('SELECT "Name" FROM "Artist"')

# cursor.execute('SELECT "Name" FROM "Artist" WHERE "Name" = %s', ["Queen"])

# cursor.execute('SELECT "Name" FROM "Artist" WHERE "ArtistId" = %s', [51])

# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# cursor.execute('SELECT * from "Artist" WHERE "Name" = %s', ["The Clash"])
cursor.execute('SELECT * from "Artist" WHERE "Name" = %s', ["Test"])

# fetch the reults (multiple)
results = cursor.fetchall()

# results = cursor.fetchone()

connection.close()

# Print the results
for result in results:
    print(result)

