import pymongo

client = pymongo.MongoClient()

db = client.RoadTrips

#create users collection
users = db.allusers

#create trips collection
trips = db.alltrips

def createUser(inputName, userPW):
	users.insert({inputName: userPW})

def checkUser(inputName, userPW):
	if users.find_one(inputName)

def createTrip(tripDict):
	trips.insert(tripDict)

def getUserTrips(inputName):
	usersTrips = trips.find('')
	return usersTrips