import pymongo

connection = pymongo.Connection()
db = pymongo.Connection().Stumblr.posts

def insert_user(userID, tags):
    #Inserts a user's informat into the collection.
    post = {"userid": userID,
    		"tags": tags,
    		"urls": {},
            "recently_visited": ['http://tumblr.com']
    		}
    #only insert if the user is not already in the collection.
    if db.find({"userid": userID}).count() == 0:
    	db.insert(post)

def recently_visited(userid):
    val = db.find_one({'userid': userid})
    return val['recently_visited']

def add_to_recently_visited(userid, site):
    val = db.find_one({'userid': userid})
    recentSites = val['recently_visited']
    recentSites.append(site)
    db.update({'userid': userid}, val)

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
    db.update({'useridhttp://tmblr.co/ZPVkJuc6heiZ':userID},val)
db.drop()
insert_user({'userid': 25}, {"Cars": 2, "Guitar": 4, "hacking": 6, "Pennapps": 10})
