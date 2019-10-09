import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

app = Flask(__name__)


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///data/BOTULISM.db")

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

@app.route("/data")
def datatable():
    """Return the data page."""
    return render_template("data.html")

@app.route("/cleanup")
def cleanup():
    """Return the data cleanup page."""
    return render_template("cleanup.html")

@app.route("/about")
def about():
    """Return the about page."""
    return render_template("about.html")

@app.route("/botulism")
def botulism():
    """Return the botulism page."""
    return render_template("botulism.html")

@app.route("/history")
def history():
    """Return the history page."""
    return render_template("history.html")

@app.route("/types")
def types():
    """Return the history page."""
    return render_template("types.html")

@app.route("/safety")
def safety():
    """Return the history page."""
    return render_template("safety.html")


@app.route("/allresults")
#Route retuns json of all records in dataset
def all():

    session = Session(engine)

    all_results = session.query(bot_data.state_name, 
                                bot_data.record_year, 
                                bot_data.BotType,
                                bot_data.ToxinType,
                                bot_data.record_count,
                                bot_data.BotId).all()

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

@app.route("/statecharts/<state>")
#Route returns data for two state charts:  bot type vs time, tox type vs time
def stateInfo(state):
    #Returns data for one specific state

    session = Session(engine)

    state_data = session.query(bot_data.state_name, 
                        bot_data.record_year, 
                        bot_data.BotType,
                        bot_data.ToxinType,
                        bot_data.record_count).filter(bot_data.state_name == state).all()
    
    session.close()

    years = []

    foodborne_bot = []
    infant_bot = []
    wound_bot = []
    other_bot = []

    unknown_tox = []
    E_tox =[]
    B_tox =[]
    A_tox =[]
    F_tox =[]
    AB_tox =[]
    Ba_tox =[]
    Bf_tox =[]
    EF_tox =[]
    ABE_tox =[]
    Ab_tox =[]
    BF_tox =[]

    for i in state_data:
        years.append(i[1])

    for i in state_data:
        if i[2] == "Foodborne":
            foodborne_bot.append(i[4])
        else:
            foodborne_bot.append('0')
            
    for i in state_data:
        if i[2] == "Infant":
            infant_bot.append(i[4])
        else:
            infant_bot.append('0')
            
    for i in state_data:
        if i[2] == "Wound":
            wound_bot.append(i[4])
        else:
            wound_bot.append('0')
            
    for i in state_data:
        if i[2] == "Other":
            other_bot.append(i[4])
        else:
            other_bot.append('0')
    
    for i in state_data:
        if i[3] == "Unknown":
            unknown_tox.append(i[4])
        else:
            unknown_tox.append('0')
        
    for i in state_data:
        if i[3] == "E":
            E_tox.append(i[4])
        else:
            E_tox.append('0')
            
    for i in state_data:
        if i[3] == "B":
            B_tox.append(i[4])
        else:
            B_tox.append('0')
            
    for i in state_data:
        if i[3] == "A":
            A_tox.append(i[4])
        else:
            A_tox.append('0')
            
    for i in state_data:
        if i[3] == "F":
            F_tox.append(i[4])
        else:
            F_tox.append('0')
            
    for i in state_data:
        if i[3] == "AB":
            AB_tox.append(i[4])
        else:
            AB_tox.append('0')
            
    for i in state_data:
        if i[3] == "Ba":
            Ba_tox.append(i[4])
        else:
            Ba_tox.append('0')
            
    for i in state_data:
        if i[3] == "Bf":
            Bf_tox.append(i[4])
        else:
            Bf_tox.append('0')
            
    for i in state_data:
        if i[3] == "EF":
            EF_tox.append(i[4])
        else:
            EF_tox.append('0')
            
    for i in state_data:
        if i[3] == "ABE":
            ABE_tox.append(i[4])
        else:
            ABE_tox.append('0')
            
    for i in state_data:
        if i[3] == "Ab":
            Ab_tox.append(i[4])
        else:
            Ab_tox.append('0')
            
    for i in state_data:
        if i[3] == "BF":
            BF_tox.append(i[4])
        else:
            BF_tox.append('0')

    state_dict = {
        "years": years,
        "foodborne": foodborne_bot,
        "infant": infant_bot,
        "wound": wound_bot,
        "other": other_bot,
        "unknownTox": unknown_tox,
        "ETox": E_tox,
        "BTox": B_tox,
        "ATox": A_tox,
        "FTox": F_tox,
        "ABTox": AB_tox,
        "BaTox": Ba_tox,
        "BfTox": Bf_tox,
        "EFTox": EF_tox,
        "ABETox": ABE_tox,
        "AbTox": Ab_tox,
        "BFTox": BF_tox
    }
    
    return jsonify(state_dict)
        

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

@app.route("/circles")
#Returns json for circlechart

def circleData():
    session = Session(engine)

    all_states = session.query(bot_data.state_name).distinct().all()

    state_names = []
    
    for i in all_states:
        for state in i:
            state_names.append(state)


    food_children = []
    for state in state_names:
    
    
        foodborne_data = session.query(bot_data.state_name,
                                bot_data.BotType,
                            bot_data.record_year,
                            func.sum(bot_data.record_count)).\
                            filter(bot_data.BotType == "Foodborne").\
                            filter(bot_data.state_name == state).\
                            group_by(bot_data.record_year).\
                            order_by(bot_data.state_name).all()
        
        children = []
        
        for i in foodborne_data:

            children.append({"name": i[2], "value": i[3]})
            

        one_state = {"name": state, "children": children}  
        food_children.append(one_state)


    infant_children = []
    for state in state_names:
    
    
        infant_data = session.query(bot_data.state_name,
                                bot_data.BotType,
                            bot_data.record_year,
                            func.sum(bot_data.record_count)).\
                            filter(bot_data.BotType == "Infant").\
                            filter(bot_data.state_name == state).\
                            group_by(bot_data.record_year).\
                            order_by(bot_data.state_name).all()
        
        children = []
        
        for i in infant_data:

            children.append({"name": i[2], "value": i[3]})
            

        one_state = {"name": state, "children": children}  
        infant_children.append(one_state)
        
    wound_children = []
    for state in state_names:
    
    
        wound_data = session.query(bot_data.state_name,
                                bot_data.BotType,
                            bot_data.record_year,
                            func.sum(bot_data.record_count)).\
                            filter(bot_data.BotType == "Wound").\
                            filter(bot_data.state_name == state).\
                            group_by(bot_data.record_year).\
                            order_by(bot_data.state_name).all()
        
        children = []
        
        for i in wound_data:

            children.append({"name": i[2], "value": i[3]})
            

        one_state = {"name": state, "children": children}  
        wound_children.append(one_state)

    other_children = []
    for state in state_names:
    
    
        other_data = session.query(bot_data.state_name,
                                bot_data.BotType,
                            bot_data.record_year,
                            func.sum(bot_data.record_count)).\
                            filter(bot_data.BotType == "Other").\
                            filter(bot_data.state_name == state).\
                            group_by(bot_data.record_year).\
                            order_by(bot_data.state_name).all()
        
        children = []
        
        for i in other_data:

            children.append({"name": i[2], "value": i[3]})
            
        one_state = {"name": state, "children": children}  
        other_children.append(one_state)

    session.close()

    json= {"name": "botulism",
       "children":[
           {
           "name": "Foodborne",
            "children": food_children
           },
           {
            "name": "Infant",
            "children": infant_children
           },
           {"name": "Wound",
            "children": wound_children
           },
           {"name": "Other",
           "children": other_children}
       ]}
    
    return jsonify(json)



@app.route("/stacey")
#Route retuns json of all records in dataset
def f_stacey():
    session = Session(engine)

    all_results = session.query(bot_data.state_name, 
                                bot_data.record_year, 
                                bot_data.BotType,
                                bot_data.ToxinType,
                                bot_data.record_count,
                                bot_data.BotId).all()

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

    
    df = pd.DataFrame(all_records)
    table = pd.pivot_table(df, values='count', index=['toxType'], columns=['botType'], aggfunc=np.sum).fillna(0).to_json()

    return jsonify(table)




if __name__ == "__main__":
    app.run()
