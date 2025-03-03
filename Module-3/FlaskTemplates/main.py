from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/templates', 'index_temp', views.index_temp)

if __name__ == '__main__':
    app.run(debug=True) 
