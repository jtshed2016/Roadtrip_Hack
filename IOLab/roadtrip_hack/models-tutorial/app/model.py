import pymongo

client = pymongo.MongoClient()

db = client.RoadTrips

#create users collection
users = db.allusers

#create trips collection
trips = db.alltrips

def createUser(inputName, userPW):
	users.insert({'username': inputName, 'userPW': userPW})

def checkUser(inputName, userPW):
	userAttempt = users.findOne(inputName)
		if userAttempt['username'] != None:
			if userAttempt['userPW'] == userAttempt['pw']:
				return 1
			else:
				return 0
		else:
			return 2


def createTrip(tripDict):
	trips.insert(tripDict)

def getUserTrips(inputName):
	usersTrips = trips.find('')
	return usersTrips