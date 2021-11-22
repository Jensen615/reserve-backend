from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rooms(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    room_name = db.Column(db.String, nullable=False)
    hall = db.Column(db.String, nullable=False)
    dates = db.Column(db.String, nullable=False)
    times = db.Column(db.String, nullable=False)
    features = db.Column(db.Boolean, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False)
    day_of_week = db.Column(db.String, nullable=False)


    def __init__(self, **kwargs):
        self.location = kwargs.get("location")
        self.room_name = kwargs.get("room_name")
        self.hall = kwargs.get("hall")
        self.dates = kwargs.get("dates")
        self.times = kwargs.get("times")
        self.features = kwargs.get("features")
        self.capacity = kwargs.get("capacity")
        self.image = kwargs.get("image")
        self.day_of_week = kwargs.get("day_of_week")
    

    def serialize(self):
        return{
        "id": self.id,
        "location": self.location,
        "room_name": self.room_name,
        "hall": self.hall,
        "dates": self.dates,
        "times": self.times,
        "features": self.features,
        "capacity": self.capacity,
        "image": self.image,
        "day_of_week": self.day_of_week,
        }

class Reservations():
    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))


def __init__(self, **kwargs):
    self.user = kwargs.get("user")
    self.time = kwargs.get("time")
    self.date = kwargs.get("date")
    self.room_id = kwargs.get("room_id")

def serialize(self):
    return{
        "id": self.id,
        "user": self.user,
        "time": self.time,
        "date": self.date,
    }

def sub_serialize(self):
    room = Rooms.query.filer_by(id=self.course_id).first()
    return{
        "id": self.id,
        "user": self.user,
        "time": self.time,
        "date": self.date,
        "room": room.serialize(),
    }

    

