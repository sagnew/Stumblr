import pymongo

connection = pymongo.Connection()
db = connection.Stumblr.posts

def insert_user(userID, tags):
    #Inserts a user's informat into the collection.
    post = {"userid": userID,
    		"tags": tags,
    		"urls": {}
    		}
    #only insert if the user is not already in the collection.
    if db.find({"userid": userID}).count() == 0:
    	db.insert(post)

def add_tags(userID, tags):
    val = db.find_one({'userid': userID})
    tagVals = val['tags']

    for t in tags:
    	if t not in tagVals.keys():
        	tagVals[t] = 0
    db.update({'userid': userID}, tagVals)

def increment_tags(userID, tags):
    val = db.find_one({'userid': userID})
    tagVals = val['tags']

    incList = []

    for t in tags:
    	if t in tagVals.keys():
    	    tagVals[t] = tagVals[t] + 1
    	else:
    		incList.append(t)
    db.update({'userid':userID},val)

def decrement_tags(userID, tags):
    val = db.find_one({'userid': userID})
    tagVals = val['tags']

    decList = []

    for t in tags:
    	if t in tagVals.keys():
    		tagVals[t] = tagVals[t] - 1
    	else:
    		decList.append(t)
    db.update({'userid':userID},val)

db.drop()

insert_user(25, {"Kung Fu": 1, "Hacking": 1})
for item in db.find():
    print item
print "  "
increment_tags(25, ["Kung Fu", "Hacking"])
for item in db.find():
    print item
print " "
decrement_tags(25, ["Kung Fu", "Hacking"])
for item in db.find():
    print item
print " "
add_tags(25, ["Fighting", "Guitar"])
for item in db.find():
    print item
