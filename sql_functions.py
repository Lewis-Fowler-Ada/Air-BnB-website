import sqlite3


def return_data_from_query(query):
  db = sqlite3.connect('airBnB.db')
  cursor = db.cursor()
  cursor.execute(query)
  data = cursor.fetchall()
  db.close()
  return data


def max_price():
  #maximum price per month
  pass


def insert_data(id, name, host_id, host_name, neighbourhood_group,
                neighbourhood, latitude, longitude, room_type, price,
                minimum_nights, number_of_reviews, last_review,
                reviews_per_month, calculated_host_listings_count,
                availability_365):
  db = sqlite3.connect('airBnB.db')
  cursor = db.cursor()
  cursor.execute(
    '''
    INSERT INTO listings(
      id,
      name,
      host_id,
      host_name,
      neighbourhood_group,
      neighbourhood,
      latitude,
      longitude,
      room_type,
      price,
      minimum_nights,
      number_of_reviews,
      last_review,
      reviews_per_month,
      calculated_host_listings_count,
      availability_365
    )
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) 
    ''', (id, name, host_id, host_name, neighbourhood_group, neighbourhood,
          latitude, longitude, room_type, price, minimum_nights,
          number_of_reviews, last_review, reviews_per_month,
          calculated_host_listings_count, availability_365))

  db.commit()
  db.close()


def return_all():
  db = sqlite3.connect('airBnB.db')
  cursor = db.cursor()
  cursor.execute('''SELECT * FROM listings ''')
  listings = cursor.fetchall()
  db.close()
  return listings