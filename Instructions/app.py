import numpy as np


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine('sqlite:////Users/jdwhite/SQLalchemy_challenge/Instructions/Resources/hawaii.sqlite')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Surf's Up Climate API<br/>"
        f"Available Routes (Use YYYY-MM-DD format for start and end dates):<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api.v1.0/stations<br/>"
        f"/api.v1.0/tobs<br/>"
        f"/api.v1.0/$lt;start&gt;<br/>"
        f"/api.v1.0/$lt;start&gt;/&lt;end&gt;"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    sel = [Measurement.id,Measurement.station,Measurement.date,Measurement.prcp,Measurement.tobs]
    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(*sel).all()

    #Dictionary for row data and append
    all_precipitation = []
    for precipitation in results:
        precipitation_dict = {}
        precipitation_dict = precipitation.id
        precipitation_dict = precipitation.date
        precipitation_dict = precipitation.prcp
        precipitation_dict = precipitation.tobs
        all_precipitation.append(precipitation_dict)

    session.close()
    return jsonify(all_precipitation)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(Station.station, Station.name).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = []
    for station in stations: 
        station_dict = {}
        station_dict = station.id
        station_dict = station.station
        station_dict = station.name
        station_dict = station.latitude
        station_dict = station.longitude
        station_dict = station.elevation
        all_stations.append(station_dict)
    session.close()
    return jsonify(all_stations)


if __name__ == '__main__':
    app.run(debug=True)
