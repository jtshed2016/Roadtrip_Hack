import pymongo

client = pymongo.MongoClient()

db = client.RoadTrips

#create users collection
users = db.allusers

#create trips collection
trips = db.alltrips

def checkUser