from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import backend
import os

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/stumbl', methods=['POST', 'GET'])
def stumbl():
    url = backend.getNextUrl()
    print url
    return render_template('stumbl.html', url = url)

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
	app.run(host='0.0.0.0', port=port, debug=True)
