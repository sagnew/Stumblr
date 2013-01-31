from flask import Flask
from flask import render_template
from flask import request
import backend
import os
import sendgrid
import mongoFunctions
import urllib2
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('stumbl.html', user = '', tag = '', url='http://tumblr.com', favorites = {})

@app.route('/stumbl', methods=['POST', 'GET'])
def stumbl():
    userid = request.form['prompt']
    tags = request.form['interests']
    if userid == '':
        return render_template('stumbl.html', user = '', tag = '', url='http://tumblr.com')
    tags = tags.split(',')

    if " separated by commas" in tags:
        tags = ['hacking']

    try:
        for tag in backend.retrieveLikes(userid):
            tags.append(tag)
    except urllib2.HTTPError:
        tags = tags


    mongoFunctions.insert_user(userid, tags)
    mongoFunctions.update_tags(userid, tags, 0)
    url, tag = backend.getUrl(mongoFunctions.get_tags(userid), userid)
    mongoFunctions.add_to_recently_visited(userid, url)
    favList = mongoFunctions.get_favorites(userid)
    return render_template('stumbl.html', url = url, tag = tag, user = userid, favorites = favList)

@app.route('/like', methods=['POST', 'GET'])
def like():
    url = request.form['url']
    tag = request.form['tag']
    tags = []
    tags.append(tag)
    userid = request.form['prompt']
    favList = mongoFunctions.get_favorites(userid)
    mongoFunctions.update_tags(userid, tags, 1)
    return render_template('stumbl.html', url = url, tag = tag, user = userid, favorites = favList)

@app.route('/dislike', methods=['POST', 'GET'])
def dislike():
    url = request.form['url']
    userid = request.form['prompt']
    tag = request.form['tag']
    tags = []
    tags.append(tag)
    favList = mongoFunctions.get_favorites(userid)
    mongoFunctions.update_tags(userid, tags, -1)
    return render_template('stumbl.html', url = url, tag = tag, user = userid, favorites = favList)

@app.route('/favorites', methods=['POST', 'GET'])
def favorites():
    url = request.form['url']
    userid = request.form['prompt']
    tag = request.form['tag']
    title = request.form['title']
    mongoFunctions.add_to_favorites(userid, url, title)
    favList = mongoFunctions.get_favorites(userid)
    return render_template('stumbl.html', url = url, tag = tag, user = userid, favorites = favList)

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port, debug=True)
