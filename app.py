#import dependencies 
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask

#set up the DB connection like in Jupyter Notebook
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

#reflect database
Base.prepare(engine, reflect=True)

#create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link
session = Session(engine)

#set up Flask App
app = Flask(__name__)

#establish the welcome route for Flask
@app.route("/")

#create a welcome function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#create precipitation path
@app.route("/api/v1.0/precipitation")

#create precipitation function - date and precip form prior year
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return (precip)

#create stations path
@app.route("/api/v1.0/stations")

#create station functionflask run

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return (stations)

#create app route for temps
@app.route("/api/v1.0/tobs")

#create temp function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return (temps)

#Current weather report
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#create stas function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return (temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return (temps)