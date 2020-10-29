from flask import render_template, request
from app import app
from app.models.calendar import events, add_new_event
from app.models.event import *

@app.route('/')
def index():
    return render_template("index.html", events=events)

@app.route('/add-event', methods=['GET', 'POST'])
def add_event():  
    date = request.form['date']
    event_name = request.form['event_name']
    guest_numbers = request.form['guest_numbers']
    room_location = request.form['room_location']
    description = request.form['description']
    new_event = Event(date=date, event_name=event_name, guest_numbers=guest_numbers, room_location=room_location, description=description, recurring=False)
    add_new_event(new_event)
    return render_template('index.html', events=events)