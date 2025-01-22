from flask import Flask

# WSGI application ( Web Server Gateway Interface)
app = Flask(__name__)

@app.route("/")
def welcome():
    return "This is home page"

@app.route("/index")
def index():
    return " This is our index page"


if __name__=="__main__":
    app.run(debug=True)
