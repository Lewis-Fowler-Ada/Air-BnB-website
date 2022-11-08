from flask import Flask, render_template, request, redirect, url_for
import sql_functions

print(sql_functions.return_all())
listing_file = open('listings_summary.csv', 'r')
for line in listing_file:
  line = line.split(',')
  try:
    id = line[0]
    name = line[1]
    host_id = line[2]
    host_name = line[3]
    neighbourhood_group = line[4]
    neighbourhood = line[5]
    latitude = line[6]
    longitude = line[7]
    room_type = line[8]
    price = line[9]
    minimum_nights = line[10]
    number_of_reviews = line[11]
    last_review = line[12]
    reviews_per_month = line[13]
    calculated_host_listings_count = line[14]
    availability_365 = line[15]
    sql_functions.insert_data(id, name, host_id, host_name,
                              neighbourhood_group, neighbourhood, latitude,
                              longitude, room_type, price, minimum_nights,
                              number_of_reviews, last_review,
                              reviews_per_month,
                              calculated_host_listings_count, availability_365)
  except:
    pass
print(sql_functions.return_all())

# app = Flask(  # Create a flask app
#   __name__,
#   template_folder='templates',  # Name of html file folder
#   static_folder='static'  # Name of directory for static files
# )

# @app.route('/', methods=["GET", "POST"])
# def home_page():
#   return render_template("home_page.html")

# if __name__ == "__main__":
#   app.run(  # Starts the site
#     host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
#     port=80)
