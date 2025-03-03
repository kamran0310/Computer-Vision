from flask import render_template
def index():
    return "Welcome to the homepage"

def index_temp():
    return render_template('index.html')