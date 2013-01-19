"""
Python helper functions
This file should be placed on project root directory
"""
import shutil
from urllib import urlretrieve
import os

#Set up the database
connection = pymongo.Connection('mongodb://santa:balls@linus.mongohq.com:10040/secret_santa')
db = connection.Stumblr
collection = db.Users

#Inserts a user, and related data into the db
def insert_into_db(name, tags):
	#Inserts a user's information into the collection
	post = {"name": name,
			 "tags": tags
		   }
	#Only insert if the user is not already in the collection
	if collection.find({"name": name}).count() == 0:
		collection.insert(post)

#Updates tags in the database. Input is a python list of tags
def increment_tags(user, tags):
    tagList = collection.find({'tags'})
    updated = []
    for tag in tags:
        #This entire method makes no sense. Finish it later
        collection.update({'tags': updated})

# recursively removes the folder named userId
def clearUserFiles(userId):
    shutil.rmtree('./%s' % userId)

# download file to userId/filename
def pullFile(url, userId, filename):
    path = "./%s/%s" % (userId, filename)
    try:
        urlretrieve(url, path)
    except IOError:
        addUser(userId)
        urlretrieve(url, path)

# create user (on login)
def addUser(userId):
    directory = "./%s" % userId
    if not os.path.exists(directory):
        os.makedirs(directory)
