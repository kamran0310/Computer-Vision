from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "our first flask app"

@app.route('/route1')
def route1():
    return "This function is executed from route 1"

def route2():
    return "this function is executed from route2"
app.add_url_rule('/route2', 'route2', route2)
if __name__ == "__main__":
    app.run(debug=True)
