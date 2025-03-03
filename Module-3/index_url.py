from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is homepage"

#variable rules

@app.route('/<name>')
def variable(name):
    return "This is a variable name: {}".format(name)

@app.route('/blog/<int:blogid>')
def blog(blogid):
    return "blogid is: {}".format(blogid)

@app.route('/weight/<float:w>')
def weight(w):
    return "Your weight is: %s"%w

if __name__ == "__main__":
    app.run(debug=True)
    