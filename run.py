import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/about')
def about():
    data = []
    with open("data/verzorgers.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", verzorgers=data)
@app.route('/contact')
def contact():
    return render_template("contact.html", page_title="Contact")
@app.route('/careers')
def career():
    return render_template("careers.html", page_title="Walk with us")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

# import os
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello, World"


#     if __name__=="__main__":
#         app.run(host=os.environ.get("IP"),
#                 port=int(os.environ.get("PORT")),
#                 debug=True)