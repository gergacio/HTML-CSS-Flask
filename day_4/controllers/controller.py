from crypt import methods
from flask import render_template, request, redirect
from app import app
from models.todo_list import *
from models.event import Event
import datetime

#when browser face this route run the func (bandle)
@app.route("/events")
def index():
    return render_template("index.html", title="Annual Events", events=events)


@app.route("/events", methods=["POST"])
def add_new_event(): 
    #get staff from outside
    #date like string turn into datetime obj
    date = request.form["date"]
    split_date = date.split("/")
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    event_name = request.form["event_name"]
    number_guests = request.form["number_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    #date : date (key:value),give value to each property !!
    new_event = Event(date = date, event_name = event_name, number_guests = number_guests, room_location = room_location, description = description)
    #add_events make it in todo_list file
    add_events(new_event)
    #redirect to same route
    return redirect("/events")

@app.route("/events/delete/<name>",methods=["POST"])
def delete_event_by_name(name): 
    
    delete_event(name) 
    return redirect("/events")   

