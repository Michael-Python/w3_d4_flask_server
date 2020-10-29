from app.models.event import *

event1 = Event("31-12-2020", "Hogmanay", 100000, "Princes Street", "Party for the New Year", True)
event2 = Event("12-02-2020", "CodeClan Graduation", 18, "Martin Wishart", "Final celebrations for learning!!", False)
events = [event1, event2]

def add_new_event(event):
    events.append(event)

