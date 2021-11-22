from db import db
import json

from flask import Flask
from flask import request

from db import Rooms
from db import Reservations

app = Flask(__name__)
db_filename = "reserve.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


def success_response(data, code=200):
    return json.dumps(data), code


def failure_response(data, code=404):
    return json.dumps({"error": data}), code


@app.route("/rooms/")
def get_rooms():
    rooms = [r.serialize() for r in Rooms.query.all()]
    return success_response(rooms)


@app.route("/rooms/<int:room_id>/")
def get_room_by_id(room_id):
    room = Rooms.query.filter_by(id=id).first()
    if room is None:
        return failure_response("Room not found!")
    return success_response(room.serialize())


@app.route("/rooms/", methods=["POST"])
def create_room():
    body = json.loads(request.data)
    location = body.get("location")
    room_name = body.get("room_name")
    hall = body.get("hall")
    dates = body.get("dates")
    times = body.get("times")
    features = body.get("features", False)
    capacity = body.get("capacity")
    image = body.get("image")
    day_of_week = body.get("dow")

    if not (location and room_name and hall):
        return failure_response("Missing location or room name or hall name!", 400)
    if not capacity:
        return failure_response("Missing capacity field!", 400)

    new_room = Rooms(location, room_name, hall, dates, times,
                     features, capacity, image, day_of_week)
    db.session.add(new_room)
    db.session.commit()
    return success_response(new_room.serialize(), 201)

@app.route("/rooms/<int:room_id>/", methods=["DELETE"])
def delete_room(room_id):
    room = Reservations.query.filter_by(id=room_id).first()
    if room is None:
        return failure_response("Reservation not found!")
    db.session.delete(room)
    db.session.commit()
    return success_response(room.serialize())



@app.route("/reservations/")
def get_rsvps():
    rsvps = [r.serialize() for r in Reservations.query.all()]
    return success_response(rsvps)


@app.route("/reservations/<int:rsvp_id>/")
def get_rsvp_by_id(rsvp_id):
    rsvp = Reservations.query.filter_by(id=id).first()
    if rsvp is None:
        return failure_response("Reservation not found!")
    return success_response(rsvp.serialize())


@app.route("/reservations/<int:room_id>", methods=["POST"])
def create_rsvp(room_id):
    room = Rooms.query.filter_by(id=room_id).first()
    if room is None:
        return failure_response("Room not found!")
    body = json.laods(request.data)
    user_id = body.get("user")
    time = body.get("time")
    date = body.get("date")

    if not user_id:
        return failure_response("Missing user field!", 400)
    if not (time and date):
        return failure_response("Missing time or date field!", 400)

    new_rsvp = Reservations(user_id, time, date, room_id)
    db.session.add(new_rsvp)
    db.session.commit()
    return success_response(new_rsvp.sub_serialize(), 201)


@app.route("/reservations/<int:rsvp_id>/", methods=["DELETE"])
def delete_rsvp(rsvp_id):
    rsvp = Reservations.query.filter_by(id=id).first()
    if rsvp is None:
        return failure_response("Reservation not found!")
    db.session.delete(rsvp)
    db.session.commit()
    return success_response(rsvp.serialize())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
