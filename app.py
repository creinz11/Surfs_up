export FLASK_APP=app.py#import dependencies 
from flask import Flask

#Create new flask instance
app = Flask(__name__)

#create flask routes
@app.route('/')
def hello_world():
    return 'Hello World' 
