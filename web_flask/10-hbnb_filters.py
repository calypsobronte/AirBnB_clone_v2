#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters_hbnb():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run()