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
	return render_template('index.html')

@app.route('/stumbl', methods=['POST', 'GET'])
def stumbl():
    #userid = request.form['userID']
    userid = 25
    url, tag = backend.getUrl(mongoFunctions.get_tags(userid), userid)
    return render_template('stumbl.html', url = url, tag = tag)

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
    return render_template('stumbl.html', url = url, tag = tag)

@app.route('/dislike', methods=['POST', 'GET'])
def dislike():
    url = request.form['url']
    #tumblr api call to get tags off of url
    #userid = request.form['userID']
    userid = 25
    tag = request.form['tag']
    tags = []
    tags.append(tag)
    mongoFunctions.decrement_tags(userid, tags, -1)
    return render_template('stumbl.html', url = url, tag = tag)

@app.route('/favorites', methods=['POST', 'GET'])
def favorites():
    url = request.form['url']
    #userid = request.form['userID']
    tag = request.form['tag']
    userid = 25
    mongoFunctions.add_to_favorites(userid, url)
    return render_template('stumbl.html', url = url, tag = tag)

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port, debug=True)
