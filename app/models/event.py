class Event():

    def __init__(self, date, event_name, guest_numbers, room_location, description, recurring):
        self.date = date
        self.event_name = event_name
        self.guest_numbers = guest_numbers
        self.room_location = room_location
        self.description = description
        self.recurring = recurring
    