from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for

import os

app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/stumbl', methods=['POST', 'GET'])
def stumbl():
    with open('templates/stumbl.html', 'w') as page:
        with open('index.html') as original:
            #Do string shit to replace iframe url
            replacement = original.read().replace("", "")

	return render_template('stumbl.html')

@app.route('/test', methods=['POST', 'GET'])
def test():
	return render_template('test.html')


if __name__ == '__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port)

