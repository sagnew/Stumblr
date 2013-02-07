"""
Python helper functions
This file should be placed on project root directory
"""
import shutil
from urllib import urlretrieve
import os
import pymongo
import urllib2
#from random import randint, choice
import random
import json
import mongoFunctions


tagDict = {}
userDict = {}


def retrieveTagUrls(tagname, urlType='short_url'):
	'''Retrieves urls for specified tag'''
	try:

		url = "http://api.tumblr.com/v2/tagged?tag=" + tagname + "&api_key=fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4"
		jdata = urlConn(url)
		urlList = []

		for x in xrange(0, len(jdata['response'])):
			urlList.append(jdata['response'][x][urlType])  #or 'post_url'

		return urlList
	except:
		return ""


def retrieveLikes(username):
	''' Retrieves likes of specified user'''

	url = "http://api.tumblr.com/v2/blog/" + username + ".tumblr.com/likes?api_key=fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4"
	jdata = urlConn(url)
	likedTags = []

	#print "\n\n"

	#return jdata['response']['liked_posts'][0]['tags']
	#print jdata

	for x in xrange(0, len(jdata['response']['liked_posts'])):
		tempLikes = jdata['response']['liked_posts'][x]['tags']

		for tempLike in tempLikes:
			likedTags.append(tempLike)

	return likedTags

def urlConn(url):
	''' Gets jason object from url (api call)'''

	req = urllib2.Request(url)
	rsp = urllib2.urlopen(req)
	content = rsp.read()
	jdata = json.loads(content)
	#print jdata
	return jdata

def printUrls(userDict):
	''' Prints Urls of specified user dictionary'''

	for k in userDict.keys():
		print "Tag: " + k + "..."
		for url in userDict[k]:
			print url + "\n"
		print "\n\n"


def loadTags(tagDict):
	''' Load tags from specified tag dictionary'''
	#userDict = {}

	for tag in tagDict.keys():
		#print "Receiving data for tag: " + tag + "..."
		results = retrieveTagUrls(tag)
		userDict[tag] = results
	#printUrls(userDict)

def getNextUrl():
	#keyNum = randint(0, len(userDict.keys())-1)
	#linkNum = randint(0,len(userDict.keys()[keyNum])-1)
	#print "Picture number " + str(keyNum) + "," + str(linkNum) + ":"
	#return userDict[userDict.keys()[keyNum]][linkNum]
	build_data()
	tempLink = ""

	while tempLink == "":
		try:
			tempKey = random.choice(userDict.keys())
			tempLink = random.choice(userDict[tempKey])
		except:
			tempLink = ""

	return tempLink


def auth():
	REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
	AUTHORIZATION_URL = 'http://www.tumblr.com/oauth/authorize'
	ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
	CONSUMER_KEY = '2WJiWpzEmdfDPDFDvoBnwvC6L9AwJqD4A78MOg82zPAYQJryhZ'
	CONSUMER_SECRET = 'your_consumer_secret'

	consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
	client = oauth2.Client(consumer)

	#Step 1
	resp, content = client.request(REQUEST_TOKEN_URL, "GET")

	request_token = dict(urlparse.parse_qsl(content))
	print "Request Token:"
	print "    - oauth_token        = %s" % request_token['oauth_token']
	print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']

	#Step 2
	print "Go to the following link in your browser:"
	print "%s?oauth_token=%s" % (AUTHORIZATION_URL, request_token['oauth_token'])

def build_data():
	likesList = retrieveLikes("Jaguar7444")
	tagDict = {}

	for item in likesList:
		tagDict[item] = 0

	loadTags(tagDict)

#Alternative to Ruell's function
#Receives a python dict as input with weighted tags
def getUrl(tags, userid, count=0):
    if count > 100:
        return random.choice(recently_visited(userid)), "invalid_tag"
    weightedList = []
    recently_visited = mongoFunctions.recently_visited(userid)
    for tag in tags:
        x = 0
        while x < tags[tag]:
            weightedList.append(tag)
            x += 1

    chosenTag = 'hacking'

    if not weightedList == []:
        chosenTag = random.choice(weightedList)

    Urls = retrieveTagUrls(chosenTag)
    if len(Urls) == 0:
        del tags[chosenTag]
        mongoFunctions.replace_tags(userid, tags)
        Urls = ['http://tumblr.com']

    choice = random.choice(Urls)
    Urls.remove(choice)
    x = 0
    while choice in recently_visited:
        choice = random.choice(Urls)
        Urls.remove(choice)
        x += 1
        if x > 100:
            #Try again
            return getURL(tags, userid, count + 1)
    return choice, chosenTag

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
