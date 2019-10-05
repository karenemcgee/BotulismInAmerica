import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template


app = Flask(__name__)


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Project2/data/BOTULISM.db")

Base = automap_base()
Base.prepare(engine, reflect=True)

# Save reference to Botulism table
bot_data = Base.classes.BOTULISM


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/allresults")
#Route retuns json of all records in dataset
def all():

    session = Session(engine)

    all_results = session.query(bot_data.state_name, 
                                bot_data.record_year, 
                                bot_data.BotType,
                                bot_data.ToxinType,
                                bot_data.record_count,
                                bot_data.BotID).all()

    session.close()

    all_records = []

    for state, year, botType, toxType, count, botID in all_results:
        results_dict = {}
        results_dict["state"] = state
        results_dict["year"] = year
        results_dict["botType"] = botType
        results_dict["toxType"] = toxType
        results_dict["count"] = count
        results_dict["botID"] = botID
        all_records.append(results_dict)

    return jsonify(all_records)

@app.route("/states")
#Route returns list of unique state names
def statenames():

    session = Session(engine)

    all_states = session.query(bot_data.state_name).distinct().all()

    session.close()

    state_names = []

    for i in all_states:
        for state in i:
            #create dict here if necessary to work in app
            state_names.append(state)

    return jsonify(state_names)

@app.route("/bottypes")
#Route returns list of unique Botulism types
def botTypes():

    session = Session(engine)

    all_botTypes = session.query(bot_data.BotType).distinct().all()

    session.close()

    bot_types = []

    for i in all_botTypes:
        for kind in i:
            #create dict here if necessary to work in app
            bot_types.append(kind)
     
    return jsonify(bot_types)  

@app.route("/toxtypes")
#Route returns list of unique toxin types
def toxTypes():

    session = Session(engine)

    all_toxTypes = session.query(bot_data.ToxinType).distinct().all()

    session.close()

    tox_types = []

    for i in all_toxTypes:
        for kind in i:
            #create dict here if necessary to work in app
            tox_types.append(kind)

    return jsonify(tox_types)

@app.route("/years")
#Returns list of unique years

def record_years():

    session = Session(engine)

    all_years = session.query(bot_data.record_year).order_by(bot_data.record_year).distinct().all()

    session.close()

    years = []

    for i in all_years:
        for year in i:
            #create dict here if necessary to work in app
            years.append(year)


    return jsonify(years)


if __name__ == "__main__":
    app.run()
