from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Rooms(db.Model):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    room_name = db.Column(db.String, nullable=False)
    hall = db.Column(db.String, nullable=False)
    # times = db.Column(db.Integer, db.ForeignKey("times.id"))
    features = db.Column(db.Boolean, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=True)
    # day_of_week = db.Column(db.String, nullable=False)
    # reservations = db.relationship("reservations", cascade="delete")

    def __init__(self, **kwargs):
        self.location = kwargs.get("location")
        self.room_name = kwargs.get("room_name")
        self.hall = kwargs.get("hall")
        # self.times = kwargs.get("times")
        self.features = kwargs.get("features")
        self.capacity = kwargs.get("capacity")
        self.image = kwargs.get("image")
        # self.day_of_week = kwargs.get("day_of_week")

    def serialize(self):
        return{
            "id": self.id,
            "location": self.location,
            "room_name": self.room_name,
            "hall": self.hall,
            # "times": self.times,
            "features": self.features,
            "capacity": self.capacity,
            "image": self.image,
            # "day_of_week": self.day_of_week
        }


class Reservations(db.Model):
    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))
    time = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        self.user = kwargs.get("user")
        self.room_id = kwargs.get("room_id")
        self.time = kwargs.get("time")
        self.date = kwargs.get("date")

    def serialize(self):
        return{
            "id": self.id,
            "user": self.user,
            "time": self.time,
            "date": self.date
        }

    def sub_serialize(self):
        room = Rooms.query.filter_by(id=self.room_id).first()
        return{
            "id": self.id,
            "user": self.user,
            "time": self.time,
            "date": self.date,
            "room": room.serialize()
        }


class Times(db.Model):
    __tablename__ = "times"
    id = db.Column(db.Integer, primary_key=True)
    t1 = db.Column(db.Boolean, nullable=False)
    t2 = db.Column(db.Boolean, nullable=False)
    t3 = db.Column(db.Boolean, nullable=False)
    t4 = db.Column(db.Boolean, nullable=False)
    t5 = db.Column(db.Boolean, nullable=False)
    t6 = db.Column(db.Boolean, nullable=False)
    t7 = db.Column(db.Boolean, nullable=False)
    t8 = db.Column(db.Boolean, nullable=False)
    t9 = db.Column(db.Boolean, nullable=False)
    t10 = db.Column(db.Boolean, nullable=False)
    t11 = db.Column(db.Boolean, nullable=False)
    t12 = db.Column(db.Boolean, nullable=False)
    t13 = db.Column(db.Boolean, nullable=False)
    t14 = db.Column(db.Boolean, nullable=False)
    t15 = db.Column(db.Boolean, nullable=False)
    t16 = db.Column(db.Boolean, nullable=False)
    t17 = db.Column(db.Boolean, nullable=False)
    t18 = db.Column(db.Boolean, nullable=False)
    t19 = db.Column(db.Boolean, nullable=False)
    t20 = db.Column(db.Boolean, nullable=False)
    t21 = db.Column(db.Boolean, nullable=False)
    t22 = db.Column(db.Boolean, nullable=False)
    t23 = db.Column(db.Boolean, nullable=False)
    t24 = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.String, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))

    def __init__(self, **kwargs):
        self.t1 = kwargs.get("t1", False)
        self.t2 = kwargs.get("t2", False)
        self.t3 = kwargs.get("t3", False)
        self.t4 = kwargs.get("t4", False)
        self.t5 = kwargs.get("t5", False)
        self.t6 = kwargs.get("t6", False)
        self.t7 = kwargs.get("t7", False)
        self.t8 = kwargs.get("t8", False)
        self.t9 = kwargs.get("t9", False)
        self.t10 = kwargs.get("t10", False)
        self.t11 = kwargs.get("t11", False)
        self.t12 = kwargs.get("t12", False)
        self.t13 = kwargs.get("t13", False)
        self.t14 = kwargs.get("t14", False)
        self.t15 = kwargs.get("t15", False)
        self.t16 = kwargs.get("t16", False)
        self.t17 = kwargs.get("t17", False)
        self.t18 = kwargs.get("t18", False)
        self.t19 = kwargs.get("t19", False)
        self.t20 = kwargs.get("t20", False)
        self.t21 = kwargs.get("t21", False)
        self.t22 = kwargs.get("t22", False)
        self.t23 = kwargs.get("t23", False)
        self.t24 = kwargs.get("t24", False)
        self.date = kwargs.get("date")
        self.room_id = kwargs.get("room_id")

    def serialize(self):
        return{
            "id": self.id,
            "t1": self.t1,
            "t2": self.t2,
            "t3": self.t3,
            "t4": self.t4,
            "t5": self.t5,
            "t6": self.t6,
            "t7": self.t7,
            "t8": self.t8,
            "t9": self.t9,
            "t10": self.t10,
            "t11": self.t11,
            "t12": self.t12,
            "t13": self.t13,
            "t14": self.t14,
            "t15": self.t15,
            "t16": self.t16,
            "t17": self.t17,
            "t18": self.t18,
            "t19": self.t19,
            "t20": self.t20,
            "t21": self.t21,
            "t22": self.t22,
            "t23": self.t23,
            "t24": self.t24,
            "date": self.date,
            "room_id": self.room_id
        }
