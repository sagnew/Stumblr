import pymongo

connection = pymongo.Connection()
db = connection.Stumblr

def insert_user(userID):
	#Inserts a user's informat into the collection.
	post = {"userID": userID,
			"tags": {},
			"urls": {}
			}
	#only insert if the user is not already in the collection.
	if db.post.find({"userID": userID}).count() == 0:
		#collection.insert(post)
		print userID

def add_tags(userID, tags):
	val = db.posts.find_one({'userid': userID})
	tagVals = val['tags']

	for t in tags:
		if t not in tagVals.keys():
			tagVals[t] = 0


def increment_tags(userID, tags):
	val = db.posts.find_one({'userid': userID})
	tagVals = val['tags']

	incList = []

	for t in tags:
		if t in tagVals.keys():
			tagVals[t] = tagVals[t] + 1
		else:
			incList.append(t)
	db.posts.update({'userid':userID},val)

def decrement_tags(userID, tags):
	val = db.posts.find_one({'userid': userID})
	tagVals = val['tags']

	decList = []

	for t in tags:
		if t in tagVals.keys():
			tagVals[t] = tagVals[t] - 1
		else:
			decList.append(t)
	db.posts.update({'userid':userID},val)
