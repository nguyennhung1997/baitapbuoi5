from flask import Flask, render_template

a = Flask(__name__)

@a.route("/")
def index():
    return render_template("index.html")

@a.route("/about")
def index():
    return render_template("about.html")

if __name__=="__main__":
   a.run(debug=True)