# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(autoload_with = engine)
# Save references to each table
measurements = base.classes.measurement
stations = base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def homepage():
    return (
        f"Homepage<br/>"
        f"All the available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    prcp_date = session.query(measurements.date,measurements.prcp).all()
    session.close()
    prcp_data_all = [{date: prcp} for date, prcp in prcp_date]
    return jsonify(prcp_data_all)

@app.route('/api/v1.0/stations')
def station():
    stations_data = session.query(stations.station).all()
    station_names = [{'station': station[0]} for station in stations_data]
    return jsonify(station_names)

@app.route('/api/v1.0/tobs')
def tobs():
    active_station_str = 'USC00519281'
    recent_date = session.query(measurements.date).order_by(measurements.date.desc()).first()
    latest_str =list(np.ravel(recent_date))[0]
    latest_date=dt.datetime.strptime(latest_str,"%Y-%m-%d")
    last_date=latest_date-dt.timedelta(days=366)
    temperature_data = session.query(measurements.tobs, measurements.date).\
    filter(measurements.station == active_station_str, measurements.date >= last_date).all()
    temperature_data = [{"date": date, "temperature": tobs} for date, tobs in temperature_data]
    return jsonify(temperature_data)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def calc_temps(start, end=None):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start (string): A date string in the format %Y-%m-%d
        end (string, optional): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    if end is None:
        end_date = session.query(func.max(measurements.date)).scalar()
    else:
        end_date = end

    results = session.query(func.min(measurements.tobs), func.avg(measurements.tobs), func.max(measurements.tobs)).\
        filter(measurements.date >= start).filter(measurements.date <= end_date).all()

    temp_obs = {
        "Min_Temp": results[0][0],
        "avg_Temp": results[0][1],
        "max_Temp": results[0][2]
    }

    return jsonify(temp_obs)

session.close()
if __name__ == '__main__':
    app.run(debug=True)