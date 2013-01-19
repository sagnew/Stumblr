import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

#Create our index or root / route
@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
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
