from db import db
import json

from flask import Flask
from flask import request

from db import Rooms
from db import Reservations
from db import Times

import os

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


@app.route("/")
def welcome():
    return "Welcome to Reserve Backend!"


@app.route("/rooms/")
def get_rooms():
    rooms = [r.serialize() for r in Rooms.query.all()]
    return success_response(rooms)


@app.route("/rooms/<int:room_id>/")
def get_room_by_id(room_id):
    room = Rooms.query.filter_by(id=room_id).first()
    if room is None:
        return failure_response("Room not found!")
    return success_response(room.serialize())


@app.route("/rooms/", methods=["POST"])
def create_room():
    body = json.loads(request.data)
    location = body.get("location")
    room_name = body.get("room_name")
    hall = body.get("hall")
    # times = body.get("times")
    features = body.get("features", False)
    capacity = body.get("capacity")
    image = body.get("image")
    # day_of_week = body.get("day_of_week")

    if not (location and room_name and hall):
        return failure_response("Missing location or room name or hall name!", 400)
    if not capacity:
        return failure_response("Missing capacity field!", 400)

    new_room = Rooms(location=location, room_name=room_name,
                     hall=hall, features=features, capacity=capacity, image=image)
    db.session.add(new_room)
    db.session.commit()
    return success_response(new_room.serialize(), 201)


@app.route("/rooms/<int:room_id>/", methods=["POST"])
def update_room(room_id):
    room = Rooms.query.filter_by(id=room_id).first()
    if room is None:
        return failure_response("Room not found!")

    body = json.loads(request.data)
    room.location = body.get('location', room.location)
    room.room_name = body.get('room_name', room.room_name)
    room.hall = body.get('hall', room.hall)
    room.features = body.get('features', room.features)
    room.capacity = body.get('capacity', room.capacity)
    room.image = body.get('image', room.image)

    db.session.commit()
    return success_response(room.serialize())


@app.route("/rooms/<int:room_id>/", methods=["DELETE"])
def delete_room(room_id):
    room = Rooms.query.filter_by(id=room_id).first()
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
    rsvp = Reservations.query.filter_by(id=rsvp_id).first()
    if rsvp is None:
        return failure_response("Reservation not found!")
    return success_response(rsvp.serialize())


@app.route("/reservations/", methods=["POST"])
def create_rsvp():
    body = json.loads(request.data)
    room_id = body.get("room_id")
    if room_id is None:
        return failure_response("Missing room_id field!", 400)
    room = Rooms.query.filter_by(id=room_id).first()
    if room is None:
        return failure_response("Room not found!")
    user = body.get("user")
    time = body.get("time")
    date = body.get("date")

    if not user:
        return failure_response("Missing user field!", 400)
    if not (time and date):
        return failure_response("Missing time or date field!", 400)

    # time_row = Times.query.filter_by(room_id=room_id, date=date).first()
    # new_time_row = Times(date=date, room_id=room_id)

    ### Janky code to create time_row in Times table for each new rsvp... gets job done ###
    if time == 1:
        if Times.query.filter_by(t1=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t1=True, date=date, room_id=room_id)
    elif time == 2:
        if Times.query.filter_by(t2=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t2=True, date=date, room_id=room_id)
    elif time == 3:
        if Times.query.filter_by(t3=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t3=True, date=date, room_id=room_id)
    elif time == 4:
        if Times.query.filter_by(t4=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t4=True, date=date, room_id=room_id)
    elif time == 5:
        if Times.query.filter_by(t5=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t5=True, date=date, room_id=room_id)
    elif time == 6:
        if Times.query.filter_by(t6=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t6=True, date=date, room_id=room_id)
    elif time == 7:
        if Times.query.filter_by(t7=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t7=True, date=date, room_id=room_id)
    elif time == 8:
        if Times.query.filter_by(t8=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t8=True, date=date, room_id=room_id)
    elif time == 9:
        if Times.query.filter_by(t9=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t9=True, date=date, room_id=room_id)
    elif time == 10:
        if Times.query.filter_by(t10=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t10=True, date=date, room_id=room_id)
    elif time == 11:
        if Times.query.filter_by(t11=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t11=True, date=date, room_id=room_id)
    elif time == 12:
        if Times.query.filter_by(t12=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t12=True, date=date, room_id=room_id)
    elif time == 13:
        if Times.query.filter_by(t13=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t13=True, date=date, room_id=room_id)
    elif time == 14:
        if Times.query.filter_by(t14=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t14=True, date=date, room_id=room_id)
    elif time == 15:
        if Times.query.filter_by(t15=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t15=True, date=date, room_id=room_id)
    elif time == 16:
        if Times.query.filter_by(t16=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t16=True, date=date, room_id=room_id)
    elif time == 17:
        if Times.query.filter_by(t17=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t17=True, date=date, room_id=room_id)
    elif time == 18:
        if Times.query.filter_by(t18=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t18=True, date=date, room_id=room_id)
    elif time == 19:
        if Times.query.filter_by(t19=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t19=True, date=date, room_id=room_id)
    elif time == 20:
        if Times.query.filter_by(t20=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t20=True, date=date, room_id=room_id)
    elif time == 21:
        if Times.query.filter_by(t21=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t21=True, date=date, room_id=room_id)
    elif time == 22:
        if Times.query.filter_by(t22=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t22=True, date=date, room_id=room_id)
    elif time == 23:
        if Times.query.filter_by(t23=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t23=True, date=date, room_id=room_id)
    else:
        if Times.query.filter_by(t24=True, date=date, room_id=room_id).first() is not None:
            return failure_response("Time row already exists!", 400)
        new_time_row = Times(t24=True, date=date, room_id=room_id)

    if Reservations.query.filter_by(room_id=room_id, time=time, date=date).first() is not None:
        return failure_response("RSVP already exists!", 400)
    new_rsvp = Reservations(user=user, room_id=room_id, time=time,
                            date=date)

    db.session.add(new_rsvp)
    db.session.add(new_time_row)
    db.session.commit()
    return success_response(new_rsvp.sub_serialize(), 201)


@app.route("/reservations/<int:rsvp_id>/", methods=["POST"])
def update_rsvp_time(rsvp_id):
    rsvp = Reservations.query.filter_by(id=rsvp_id).first()
    if rsvp is None:
        return failure_response("Reservation not found!")

    body = json.loads(request.data)
    rsvp.user = body.get('user', rsvp.user)
    orig_time = rsvp.time
    rsvp.time = body.get('time', rsvp.time)

    # We don't allow changing rooms when updating rsvp.
    # Simply delete rsvp and create new one with new room.

    # room_id = body.get('room_id', rsvp.room_id)
    # room = Rooms.query.filter_by(id=room_id).first()
    # if room is None:
    #     return failure_response("Room not found!")
    # rsvp.room_id = room_id

    # We don't allow changing date when updating rsvp.
    # Simply delete rsvp and create new one with new date.

    # rsvp.date = body.get('date', rsvp.date)

    time_row = Times.query.filter_by(
        room_id=rsvp.room_id, date=rsvp.date).first()
    if orig_time != rsvp.time:
        time = rsvp.time
        if time == 1:
            time_row.t1 = True
        elif time == 2:
            time_row.t2 = True
        elif time == 3:
            time_row.t3 = True
        elif time == 4:
            time_row.t5 = True
        elif time == 5:
            time_row.t6 = True
        elif time == 6:
            time_row.t6 = True
        elif time == 7:
            time_row.t7 = True
        elif time == 8:
            time_row.t8 = True
        elif time == 9:
            time_row.t9 = True
        elif time == 10:
            time_row.t10 = True
        elif time == 11:
            time_row.t11 = True
        elif time == 12:
            time_row.t12 = True
        elif time == 13:
            time_row.t13 = True
        elif time == 14:
            time_row.t14 = True
        elif time == 15:
            time_row.t15 = True
        elif time == 16:
            time_row.t16 = True
        elif time == 17:
            time_row.t17 = True
        elif time == 18:
            time_row.t18 = True
        elif time == 19:
            time_row.t19 = True
        elif time == 20:
            time_row.t20 = True
        elif time == 21:
            time_row.t21 = True
        elif time == 22:
            time_row.t22 = True
        elif time == 23:
            time_row.t23 = True
        else:
            time_row.t24 = True

        # Make original rsvp time available again (True -> False)
        if orig_time == 1:
            time_row.t1 = False
        elif orig_time == 2:
            time_row.t2 = False
        elif orig_time == 3:
            time_row.t3 = False
        elif orig_time == 4:
            time_row.t5 = False
        elif orig_time == 5:
            time_row.t6 = False
        elif orig_time == 6:
            time_row.t6 = False
        elif orig_time == 7:
            time_row.t7 = False
        elif orig_time == 8:
            time_row.t8 = False
        elif orig_time == 9:
            time_row.t9 = False
        elif orig_time == 10:
            time_row.t10 = False
        elif orig_time == 11:
            time_row.t11 = False
        elif orig_time == 12:
            time_row.t12 = False
        elif orig_time == 13:
            time_row.t13 = False
        elif orig_time == 14:
            time_row.t14 = False
        elif orig_time == 15:
            time_row.t15 = False
        elif orig_time == 16:
            time_row.t16 = False
        elif orig_time == 17:
            time_row.t17 = False
        elif orig_time == 18:
            time_row.t18 = False
        elif orig_time == 19:
            time_row.t19 = False
        elif orig_time == 20:
            time_row.t20 = False
        elif orig_time == 21:
            time_row.t21 = False
        elif orig_time == 22:
            time_row.t22 = False
        elif orig_time == 23:
            time_row.t23 = False
        else:
            time_row.t24 = False

    db.session.commit()
    return success_response(rsvp.serialize())


@app.route("/reservations/<int:rsvp_id>/", methods=["DELETE"])
def delete_rsvp(rsvp_id):
    rsvp = Reservations.query.filter_by(id=rsvp_id).first()
    if rsvp is None:
        return failure_response("Reservation not found!")
    room_id = rsvp.room_id
    time = rsvp.time
    date = rsvp.date
    if time == 1:
        del_time_row = Times.query.filter_by(
            t1=True, date=date, room_id=room_id).first()
    elif time == 2:
        del_time_row = Times.query.filter_by(
            t2=True, date=date, room_id=room_id).first()
    elif time == 3:
        del_time_row = Times.query.filter_by(
            t3=True, date=date, room_id=room_id).first()
    elif time == 4:
        del_time_row = Times.query.filter_by(
            t4=True, date=date, room_id=room_id).first()
    elif time == 5:
        del_time_row = Times.query.filter_by(
            t5=True, date=date, room_id=room_id).first()
    elif time == 6:
        del_time_row = Times.query.filter_by(
            t6=True, date=date, room_id=room_id).first()
    elif time == 7:
        del_time_row = Times.query.filter_by(
            t7=True, date=date, room_id=room_id).first()
    elif time == 8:
        del_time_row = Times.query.filter_by(
            t8=True, date=date, room_id=room_id).first()
    elif time == 9:
        del_time_row = Times.query.filter_by(
            t9=True, date=date, room_id=room_id).first()
    elif time == 10:
        del_time_row = Times.query.filter_by(
            t10=True, date=date, room_id=room_id).first()
    elif time == 11:
        del_time_row = Times.query.filter_by(
            t11=True, date=date, room_id=room_id).first()
    elif time == 12:
        del_time_row = Times.query.filter_by(
            t12=True, date=date, room_id=room_id).first()
    elif time == 13:
        del_time_row = Times.query.filter_by(
            t13=True, date=date, room_id=room_id).first()
    elif time == 14:
        del_time_row = Times.query.filter_by(
            t14=True, date=date, room_id=room_id).first()
    elif time == 15:
        del_time_row = Times.query.filter_by(
            t15=True, date=date, room_id=room_id).first()
    elif time == 16:
        del_time_row = Times.query.filter_by(
            t16=True, date=date, room_id=room_id).first()
    elif time == 17:
        del_time_row = Times.query.filter_by(
            t17=True, date=date, room_id=room_id).first()
    elif time == 18:
        del_time_row = Times.query.filter_by(
            t18=True, date=date, room_id=room_id).first()
    elif time == 19:
        del_time_row = Times.query.filter_by(
            t19=True, date=date, room_id=room_id).first()
    elif time == 20:
        del_time_row = Times.query.filter_by(
            t20=True, date=date, room_id=room_id).first()
    elif time == 21:
        del_time_row = Times.query.filter_by(
            t21=True, date=date, room_id=room_id).first()
    elif time == 22:
        del_time_row = Times.query.filter_by(
            t22=True, date=date, room_id=room_id).first()
    elif time == 23:
        del_time_row = Times.query.filter_by(
            t23=True, date=date, room_id=room_id).first()
    else:
        del_time_row = Times.query.filter_by(
            t24=True, date=date, room_id=room_id).first()

    db.session.delete(del_time_row)
    db.session.delete(rsvp)
    db.session.commit()
    return success_response(rsvp.serialize())


@app.route("/times/")
def get_times():
    times = [t.serialize() for t in Times.query.all()]
    return success_response(times)


@app.route("/times/<int:time_id>/")
def get_time_row_by_id(time_id):
    time = Times.query.filter_by(id=time_id).first()
    if time is None:
        return failure_response("Time row not found!")
    return success_response(time.serialize())


@app.route("/times/<int:room_id>/<string:date>/<int:time>/")
def is_time_booked(room_id, date, time):
    if time == 1:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t1=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 2:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t2=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 3:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t3=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 4:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t4=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 5:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t5=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 6:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t6=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 7:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t7=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 8:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t8=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 9:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t9=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 10:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t10=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 11:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t11=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 12:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t12=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 13:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t13=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 14:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t14=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 15:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t15=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 16:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t16=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 17:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t17=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 18:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t18=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 19:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t19=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 20:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t20=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 21:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t21=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 22:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t22=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    elif time == 23:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t23=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())
    else:
        time_row = Times.query.filter_by(
            room_id=room_id, date=date, t24=True).first()
        if time_row is None:
            return failure_response("Time not booked!")
        return success_response(time_row.serialize())


@app.route("/times/", methods=["POST"])
def create_time_row():
    body = json.loads(request.data)
    room_id = body.get("room_id")
    if room_id is None:
        return failure_response("Missing room_id field!", 400)
    room = Rooms.query.filter_by(id=room_id).first()
    if room is None:
        return failure_response("Room not found!")
    date = body.get("date")
    if not (date):
        return failure_response("Missing date field!", 400)

    time_row = Times.query.filter_by(
        room_id=room_id, date=date).first()
    if time_row is not None:
        return failure_response("Time row already exists!")
    new_time_row = Times(date=date, room_id=room_id)
    db.session.add(new_time_row)
    db.session.commit()
    return success_response(new_time_row.serialize(), 201)


@app.route("/times/<int:time_id>/", methods=["POST"])
def update_time_row(time_id):
    time = Times.query.filter_by(id=time_id).first()
    if time is None:
        return failure_response("Time row not found!")

    body = json.loads(request.data)
    time.t1 = body.get('t1', time.t1)
    time.t2 = body.get('t2', time.t2)
    time.t3 = body.get('t3', time.t3)
    time.t4 = body.get('t4', time.t4)
    time.t5 = body.get('t5', time.t5)
    time.t6 = body.get('t6', time.t6)
    time.t7 = body.get('t7', time.t7)
    time.t8 = body.get('t8', time.t8)
    time.t9 = body.get('t9', time.t9)
    time.t10 = body.get('t10', time.t10)
    time.t11 = body.get('t11', time.t11)
    time.t12 = body.get('t12', time.t12)
    time.t13 = body.get('t13', time.t13)
    time.t14 = body.get('t14', time.t14)
    time.t15 = body.get('t15', time.t15)
    time.t16 = body.get('t16', time.t16)
    time.t17 = body.get('t17', time.t17)
    time.t18 = body.get('t18', time.t18)
    time.t19 = body.get('t19', time.t19)
    time.t20 = body.get('t20', time.t20)
    time.t21 = body.get('t21', time.t21)
    time.t22 = body.get('t22', time.t22)
    time.t23 = body.get('t23', time.t23)
    time.t24 = body.get('t24', time.t24)
    # we don't make changes to the available rooms and dates that exist in db already;
    # only changes are made to times to reflect which hours are currently available

    db.session.commit()
    return success_response(time.serialize())


@app.route("/times/<int:time_id>/", methods=["DELETE"])
def delete_time_row(time_id):
    time = Times.query.filter_by(id=time_id).first()
    if time is None:
        return failure_response("Time row not found!")
    db.session.delete(time)
    db.session.commit()
    return success_response(time.serialize())


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(host="0.0.0.0", port=port)
