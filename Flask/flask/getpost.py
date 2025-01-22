from flask import Flask, render_template, request

# WSGI application ( Web Server Gateway Interface)
app = Flask(__name__)

@app.route("/")
def welcome():
    return "This is home page"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods=['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f"Hello {name} !"
    
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)
