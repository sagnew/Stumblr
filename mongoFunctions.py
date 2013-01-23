import pymongo

connection = pymongo.Connection('mongodb://stumbler:pennapps@linus.mongohq.com:10061/Stumblr')
db = connection.Stumblr.Users

def insert_user(userID, tags):
    #Inserts a user's informat into the collection.
    post = {"userid": userID,
    		"tags": tags,
    		"urls": {},
            "recently_visited": ['http://tumblr.com'],
            "favorites": ['www.google.com']
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

def add_to_favorites(userid, url):
    val = db.find_one({'userid': userid})
    favorites = val['favorites']
    favorites.append(url)
    db.update({'userid': userid}, val)

def add_tags(userID, tags):
    val = db.find_one({'userid': userID})
    tagVals = val['tags']

    for t in tags:
    	if t not in tagVals.keys():
        	tagVals[t] = 0
    db.update({'userid': userID}, tagVals)

def update_tags(userID, tags, num):
    val = db.find_one({'userid': userID})
    tagVals = val['tags']

    incList = []

    for t in tags:
    	if t in tagVals.keys():
    	    tagVals[t] = tagVals[t] + num
    	else:
    		incList.append(t)
    db.update({'userid':userID},val)

def get_tags(userid):
    return db.find_one({'userid': userid})['tags']
