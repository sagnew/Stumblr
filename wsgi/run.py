import os
from flask import Flask
from flask import render_template
from flask import request

dir = os.environ['OPENSHIFT_DATA_DIR']

app = Flask(__name__)

#Create our index or root / route
@app.route("/")
@app.route("/stumbl", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def getUser():
    f = open('%s/blah' % dir, 'w')
    r = request.form['userID']
    f.write(r)
    r = request.form['accessToken']
    f.write('\n')
    f.write(r)
    f.close()
    return render_template("index.html")

@app.route("/tutorial", methods=["GET", "POST"])
def tutorial():
    notes = [{ "name": "First Note Ever",
              "author":"Angel",
              "content":"This text is coming from the content field"
               },
             { "name":"Finish this blog",
              "author":"Angel",
              "content":"Show the template control structures"
               },
             { "name":"Deploy this shit",
              "author":"Angel",
              "content":"When finished, this is the stuff"
               },

             ]
    return render_template("index.html", notes = notes)

if __name__ == "__main__":
    app.run(debug = "True")
