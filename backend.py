"""
Python helper functions
This file should be placed on project root directory
"""
import shutil
from urllib import urlretrieve
import os


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

# testing the functions

# temp names
url = "http://25.media.tumblr.com//8b46c6af3d1912f12c5197ab3c76a4ba//tumblr_mgueg9YdBe1rt72ano1_500.jpg"
userId = "userBlah"
filename = "testImage.jpg"

#sample calls:
#pullFile(url, userId, filename)
#clearUserFiles(userId)
#addUser(userId)
