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
    #userid = request.form['fb_id']
    mongoFunctions.insert_user(25, {})
    userid = 25
    url = backend.getUrl({"ninja turtles": 25, "Guitar": 5, "Pennapps": 20, "HackRU": 2, "Thrash": 3, "computer": 4, "technology": 2, "science": 3, "physics": 12, "Astronomy": 3, "Ninja Turtles": 20, "tmnt": 10 }, userid)
    return render_template('stumbl.html', url = url)

@app.route('/share', methods=['POST', 'GET'])
def share():
    sendgrid.sendmail(url='http://blog.pennapps.com/')
    return render_template('stumbl.html', url = 'http://blog.pennapps.com/')

@app.route('/like', methods=['POST', 'GET'])
def like():
    url = request.form['url']
    #tumblr api call to get tags off of url
    tags = ['ninja turtles', 'PennApps', 'HackRU']
    userid = request.form['fblogin']
    mongoFunctions.increment_tags(userid, tags)
    return render_template('stumbl.html', url = url)

@app.route('/dislike', methods=['POST', 'GET'])
def dislike():
    url = request.form['url']
    #tumblr api call to get tags off of url
    userid = request.form['fb_id']
    tags = ['ninja turtles', 'Pennapps', 'HackRU']
    mongoFunctions.decrement_tags(userid, tags)
    return render_template('stumbl.html', url = url)

@app.route('/favorites', methods=['POST', 'GET'])
def favorites():
    url = request.form['url']
    userid = request.form['fblogin']
    mongoFunctions.add_to_favs(userid, url)
    return render_template('stumbl.html', url = url)

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port, debug=True)
