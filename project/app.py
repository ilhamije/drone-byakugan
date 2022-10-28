import sys
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

# BASECOORDS = [-13.9626, 33.7741]

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
    points = Point.query.all()
    return render_template('index.html', points=points)


# @app.route('/point/<int:id>')
# def point(id):
#     points = Point.query.filter_by(id=id).all()
#     coords = [[point.latitude, point.longitude] for point in points]
#     return jsonify({"data": coords})

@app.route('/point/')
def point_all():
    points = Point.query.all()
    coords = [[point.latitude_off, point.longitude_off] for point in points]
    return jsonify({"data": coords})


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5001)
    # if len(sys.argv) > 1:
    #     if sys.argv[1] == 'mkdb':
    #         with app.app_context():
    #             db.create_all()
    #         # make_random_data(db)
    # else:
    #     app.run(debug=True)
