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

@app.route("/submit", methods=['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f"Hello {name} !"
    
    return render_template('form.html')

# Variable rule
@app.route("/success/<int:score>")
def submit(score):
    res = " "
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    return render_template('result.html',results=res)

@app.route("/successres/<int:score>")
def success(score):
    res = " "
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    
    exp = {'score':score, 'result':res}
    return render_template('result1.html',results=exp)

@app.route("/successif/<int:score>")
def successif(score):
    return render_template('result.html',results=score)


        

if __name__=="__main__":
    app.run(debug=True)
