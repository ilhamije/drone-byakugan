import sys
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
CORS(app)

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String)
    latitude_off = db.Column(db.Float)
    longitude_off = db.Column(db.Float)

    def __init__(self, id, image_name, lat, lng):
        self.id = id
        self.image_name = image_name
        self.latitude_off = lat
        self.longitude_off = lng

    def __repr__(self):
        return "<Point %d: Lat %s Lng %s>" % (self.id, self.latitude_off, self.longitude_off)

    @property
    def latitude(self):
        return self.latitude_off

    @property
    def longitude(self):
        return self.longitude_off


@app.route('/')
def index():
    return 'nothing to see here'


@app.route('/point/<int:id>')
def point(id):
    points = Point.query.filter_by(id=id).all()
    coords = [[point.latitude, point.longitude] for point in points]
    return jsonify({"data": coords})

@app.route('/point/')
def points():
    points = Point.query.all()
    data_list = []
    for point in points:
        data_dict = {}
        data_dict["id"] = point.id
        data_dict["image_name"] = point.image_name
        data_dict["latitude"] =  point.latitude
        data_dict["longitude"] = point.longitude
        data_list.append(data_dict)
    return jsonify(data_list)


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5001)
