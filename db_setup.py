import sqlite3


def db_setup():
  db = sqlite3.connect('airBnB.db')
  cursor = db.cursor()
  cursor.execute('''DROP TABLE IF EXISTS listings''')
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS listings(
    id INTEGER(10) PRIMARY KEY,
    name VARCHAR(200),
    host_id INTEGER(7),
    host_name VARCHAR(30),
    neighbourhood_group VARCHAR(30),
    neighbourhood VARCHAR(30),
    latitude FLOAT(8),
    longitude FLOAT(8),
    room_type VARCHAR(20),
    price INTEGER(7),
    minimum_nights INTEGER(5),
    number_of_reviews INTEGER(5),
    last_review DATE(10),
    reviews_per_month FLOAT(4),
    calculated_host_listings_count INTEGER(10),
    availability_365 INTEGER(4)
    );
    ''')
  db.commit()
  db.close()


db_setup()