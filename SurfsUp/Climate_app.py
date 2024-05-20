# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

#################################################
# Database Setup
#Create engine to hawii.sqlite
engine = create_engine("sqlite:///C:/Users/Krissy/Bootcamp/sqlalchemy-challenge/SurfsUp/Resources/hawaii.sqlite")
#################################################


# reflect an existing database into a new model
Base= automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement= Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
# Create app
app = Flask(__name__)

# define function
def date_prev_year():

# Create our session (link) from Python to the DB
    session= Session(engine)

#Define the most recent date in measurement dataset
#calaculate the date one year from the last date
    most_recent_date = session.query(func.max(Measurement.date)).first()[0]
    first_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

#closing session
    session.close()

#Return the date
    return(first_date)   
#################################################

#################################################
# Flask Routes
#Define what to do on the homepage
@app.route("/")
def homepage():
    return"""<h1> Welcome to Honolulu, Hawaii Climate API! </h1>
    <h3> The available routes are: </h3>
    <ul>
    <li>Precipitation: <strong>/api/v1.0/precipitation</strong></li>
    <li>Stations: <strong>/api/v1.0/stations</strong></li>
    <li>TOBS: <strong>/api/v1.0/tobs</strong></li>
    <li>To retrieve the minimum, average, and maximum tempratures for a specific start date, use <strong>/api/v1.0/&ltstart&gt</strong> (replace start date in yyyy-mm-dd format)</li>
    <li>To retrieve the minimum, average, and maximum tempratures for a specific start-end range, use <strong>/api/v1.0/&ltstart&gt/&ltend&gt</strong> (replace start date in yyyy-mm-dd format)</li>
    </ul>
    """

#Define precipitation URL
@app.route("/api/v1.0/precipitation")
def precipitation():

    #create session
    session =Session(engine)

    #query parcip data from last 12 months from the most recent date 
    prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date_prev_year()).all()

    #close session
    session.close()

    prcp_list =[]
    for date, prcp in prcp_data:
        prcp_dict={}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_list.append(prcp_dict)

    #return list for last 12 months
    return jsonify(prcp_list)

#define action on URL
@app.route("/api/v1.0/stations")
def stations():
    
    #create session
    session = Session(engine)

    #query station data from station dataset
    station_data = session.query(Station.station).all()

    #close session
    session.close()

    #convert list into normal list
    station_list = list(np.ravel(station_data))

    #return a list of jsonified station data
    return jsonify(station_list)

#define what URL response
@app.route("/api/v1.0/tobs")
def tobs():
    #create session
    session = Session(engine)

    #query tools data from past 12 months 
    tobs_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').\
                        filter(Measurement.date >= date_prev_year()).all()
    
    #close session
    session.close()

    #create a dictionary from the row data and append to a list of tobs_list
    tobs_list = []
    for date, tobs in tobs_data:
        tobs_dict= {} 
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

    #return a list of jsonified tobs data
    return jsonify(tobs_list)

#define URL action
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def cal_temp(start=None, end=None):

    #create session
    session = Session(engine)

    #list to query
    sel=[func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    #check for end date then perform task
    if end == None:

        #query the data from most recent date
        start_data = session.query(*sel).\
                            filter(Measurement.date >= start).all()
            
        #convert into list
        start_list = list(np.ravel(start_data))

        #return list of jasonified min, avg, max temps 
        return jsonify(start_list)
    else:
            
        #query data from start to end
        start_end_data = session.query(*sel).\
                            filter(Measurement.date >= start).\
                            filter(Measurement.date <= end).all()
            
        #convert list
        start_end_list = list(np.ravel(start_end_data))

        # return list of jasonified min, avg, max temps 
        return jsonify(start_end_list)
        
    #close session
    session.close()

#define main branch
if __name__ == "__main__":
    app.run(debug=True)
#################################################
