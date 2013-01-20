"""
Python helper functions
This file should be placed on project root directory
"""
import shutil
from urllib import urlretrieve
import os
#import pymongo
import urllib2
#from random import randint, choice
import random
#import oauth
import json
import shlex
import glob
from subprocess import call, Popen
import simplejson

#data_dir = os.environ['OPENSHIFT_DATA_DIR']
#Set up the database
#connection = pymongo.Connection('mongodb://santa:balls@linus.mongohq.com:10040/secret_santa')
#db = connection.Stumblr
#collection = db.Users

tagDict = {}
userDict = {}


def retrieveTagUrlsOld(tagname, urlType='short_url'):
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

        
def retrieveTagUrls(tagname, urlType='short_url'):
    '''Retrieves urls for specified tag'''
    url = "http://api.tumblr.com/v2/tagged?tag=" + tagname + "&api_key=fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4"
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    json = f.read()
    json = simplejson.loads(json)
#    json.dump('%s/json' % data_dir)
    # return a list of (post url, photo url) tuples
    try:
#        return [ (j['post_url'], j['photos'][0]['original_size']['url']) for j in json['response'] if j.has_key('photos')]
        return [ j['short_url'] for j in json['response'] if j.has_key('photos')]
    except:

        return ""


#print retrieveTagUrls('happy')


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
    #REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
    #AUTHORIZATION_URL = 'http://www.tumblr.com/oauth/authorize'
    #ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
    CONSUMER_KEY = '2WJiWpzEmdfDPDFDvoBnwvC6L9AwJqD4A78MOg82zPAYQJryhZ'
    CONSUMER_SECRET = 'your_consumer_secret'
    
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    client = oauth2.Client(consumer)
    
	#Step 1
   # resp, content = client.request(REQUEST_TOKEN_URL, "GET")
    
    request_token = dict(urlparse.parse_qsl(content))
    print "Request Token:"
    print "    - oauth_token        = %s" % request_token['oauth_token']
    print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']

	#Step 2
    print "Go to the following link in your browser:"
    #print "%s?oauth_token=%s" % (AUTHORIZATION_URL, request_token['oauth_token'])

def build_data():
    likesList = retrieveLikes("Jaguar7444")
    tagDict = {}

    for item in likesList:
        tagDict[item] = 0


        loadTags(tagDict)

	#print "Likes: " + str(likesList)
	#print "\n\n"
    
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
# def increment_tags(user, tags):
#     tagList = collection.find({'tags'})
#     updated = []
#     for tag in tags:
#         #This entire method makes no sense. Finish it later
#         collection.update({'tags': updated})

# recursively removes the folder named userId
def clearUserFiles(dataDir, userId):
    shutil.rmtree('%s/%s' % (dataDir, userId))

# download file to userId/filename
def pullFile(dataDir, url, userId, filename):
    path = "%s/%s/%s" % (dataDir, userId, filename)
    try:
        urlretrieve(url, path)
    except IOError:
        addUser(userId)
        urlretrieve(url, path)

# create user (on login)
def addUser(dataDir, userId):
    directory = "%s/%s" % (dataDir, userId)
    if not os.path.exists(directory):
        os.makedirs(directory)

# gif movie functions
def makeMovie(dataDir, lstOfNames):
    # get the first file's name (without extension)
    fnameMaster = lstOfNames[0].split('.')[0]
    
    # explode the gifs into png frames
    for prefix, fname in enumerate(lstOfNames):
        call(['convert', '-coalesce', fname, '%s%d%%05d.png' % (fnameMaster, prefix)])
    # combine to make the movie
    call(['convert', '-delay', '20', '-loop', '2', '%s*.png' % fnameMaster, 'anim.gif'])

    # clear the temp files
    cmd = 'rm -f %s/%s*.png' % (dataDir, fnameMaster)
    arg = shlex.split(cmd)
    arg = arg[:-1] + glob.glob(arg[-1])

    # This should work now
    p = Popen(arg)


#makeMovie(['some.gif', 'somec.gif', 'flower.gif'])
