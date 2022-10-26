import sys
import random
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

BASECOORDS = [-13.9626, 33.7741]

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude_off = db.Column(db.Float)
    longitude_off = db.Column(db.Float)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    area = db.relationship("Area")

    def __init__(self, id, area, lat, lng):
        self.id = id
        self.area = area
        self.latitude_off = lat
        self.longitude_off = lng

    def __repr__(self):
        return "<Point %d: Lat %s Lng %s>" % (self.id, self.latitude_off, self.longitude_off)

    @property
    def latitude(self):
        return self.latitude_off + self.area.latitude

    @property
    def longitude(self):
        return self.longitude_off + self.area.longitude


class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, id, name, lat, lng):
        self.id = id
        self.name = name
        self.latitude = lat
        self.longitude = lng


@app.route('/')
def index():
    areas = Area.query.all()
    return render_template('index.html', areas=areas)


@app.route('/area/<int:area_id>')
def area(area_id):
    points = Point.query.filter_by(area_id=area_id).all()
    coords = [[point.latitude, point.longitude] for point in points]
    return jsonify({"data": coords})


def make_random_data(db):
    NUMAREA = 5
    NUMPOINT = 10
    for x in range(NUMAREA):
        area = Area(x, "area %d" % x, BASECOORDS[0], BASECOORDS[1])
        db.session.add(area)
        for pid in range(NUMPOINT):
            lat = random.random() - 0.5
            lng = random.random() - 0.5
            row = Point(pid + NUMPOINT * x, area, lat, lng)
            db.session.add(row)
    db.session.commit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'mkdb':
            with app.app_context():
                db.create_all()
            make_random_data(db)
    else:
        app.run(debug=True)
