#!/usr/bin/python3
from flask import Flask, render_template, request_tearing_down
from models import storage, State, City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    states = storage.all(State)
    cities = storage.all(City).values()
    if id is not None:
        id = "State." + id
    return render_template("9-states.html",
                           states=states, cities=cities, id=id)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run()
