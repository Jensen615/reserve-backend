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
        self.code = kwargs.get("code")
        self.name = kwargs.get("name")
        self.location = kwargs.get("location")
        self.room_name = kwargs.get("room_name")
        self.hall = kwargs.get("hall")
        self.dates = kwargs.get("dates")
        self.times = kwargs.get("times")
        self.features = kwargs.get("features")
        self.capacity = kwargs.get("capacity")
        self.image = kwargs.get("image")
        self.day_of_week = kwargs.get("day_of_week")
    

    


    




