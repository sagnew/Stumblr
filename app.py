from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import mongoFunctions
import backend
import os
import sendgrid

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/stumbl', methods=['POST', 'GET'])
def stumbl():
    #userid = request.form['fb_id']
    mongoFunctions.insert_user(25, {})
    url = backend.getUrl({"ninja turtles": 25, "Guitar": 5, "Pennapps": 20, "HackRU": 2, "Thrash": 3, "computer": 4, "technology": 2, "science": 3, "physics": 12, "Astronomy": 3, "Ninja Turtles": 20, "tmnt": 10 }, 25)
    return render_template('stumbl.html', url = url)

@app.route('/like', methods=['POST', 'GET'])
def share():
    sendgrid.sendmail(url='http://blog.pennapps.com/')

    return render_template('stumbl.html', url = 'http://blog.pennapps.com/')

@app.route('/like', methods=['POST', 'GET'])
def like():
    return

@app.route('/dislike', methods=['POST', 'GET'])
def dislike():
    return

@app.route('/favorites', methods=['POST', 'GET'])
def favorites():
    return

@app.route('/test', methods=['POST', 'GET'])
def test():
	return render_template('test.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port)
