import pymongo
from django.conf import settings

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client['ticket_booking_db']

bookings_collection = db['bookings']

users_collection = db['user']

