# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
from flask import Flask

#################################################
# Database Setup
#################################################
path=r"C:\Users\agom2\sqlalchemy-challenge\Resources\hawaii.sqlite"
engine = create_engine(f"sqlite:///{path}", echo=False)

Base = automap_base()
Base.prepare(autoload_with=engine)
Base.classes.keys()



# reflect an existing database into a new model


Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table

measurement = Base.classes.measurement
Station = Base.classes.station

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
def welcome():
   """List all available api routes.""" 
   return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"- List of rain totals from all stations<br/>"
        f"/api/v1.0/passengers"
        f"/api/v1.0/stations<br/>"
        f"- List of Station numbers and names<br/>"
        f"/api/v1.0/tobs<br/>"
        f"- List of prior year temperatures from all stations<br/>"
        f"/api/v1.0/start<br/>"
        f"- When given the start date (YYYY-MM-DD), calculates the MIN/AVG/MAX temperature for all dates greater than and equal to the start date<br/>"
        f"/api/v1.0/start/end<br/>"
         f"- When given the start and the end date (YYYY-MM-DD), calculate the MIN/AVG/MAX temperature for dates between the start and end date inclusive<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Fetch the rainfall in precipitation"""
    
    last_date = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    rain = session.query(Measurements.date, Measurements.prcp).filter(Measurements.date > last_year).order_by(Measurements.date).all()

    rain_totals = []
    for result in rain:
        row = {}
        row["date"] = rain[0]
        row["prcp"] = rain[1]
        rain_totals.append(row)
        
    return jsonify(rain_totals)
