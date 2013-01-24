from flask import Flask
from flask import render_template
from flask import request
import backend
import os
import sendgrid
import mongoFunctions
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('stumbl.html', user = '', tag = '', url='http://tumblr.com')

@app.route('/stumbl', methods=['POST', 'GET'])
def stumbl():
    #userid = request.form['userID']
    userid = 25
    url, tag = backend.getUrl(mongoFunctions.get_tags(userid), userid)
    mongoFunctions.add_to_recently_visited(userid, url)
    tagstoadd = request.form['tagstoadd']
    mongoFunctions.add_tags(tagstoadd.split())
    return render_template('stumbl.html', url = url, tag = tag, hastags = mongoFunctions.hastags(userid))

@app.route('/like', methods=['POST', 'GET'])
def like():
    url = request.form['url']
    #tumblr api call to get tags off of url
    tag = request.form['tag']
    tags = []
    tags.append(tag)
    #userid = request.form['userID']
    userid = 25
    mongoFunctions.update_tags(userid, tags, 1)
    return render_template('stumbl.html', url = url, tag = tag, hastags = mongoFunctions.hastags(userid))

@app.route('/dislike', methods=['POST', 'GET'])
def dislike():
    url = request.form['url']
    #tumblr api call to get tags off of url
    #userid = request.form['userID']
    userid = 25
    tag = request.form['tag']
    tags = []
    tags.append(tag)
    mongoFunctions.update_tags(userid, tags, -1)
    return render_template('stumbl.html', url = url, tag = tag, hastags = mongoFunctions.hastags(userid))

@app.route('/favorites', methods=['POST', 'GET'])
def favorites():
    url = request.form['url']
    #userid = request.form['userID']
    tag = request.form['tag']
    userid = 25
    mongoFunctions.add_to_favorites(userid, url)
    return render_template('stumbl.html', url = url, tag = tag, hastags = mongoFunctions.hastags(userid))

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port, debug=True)
