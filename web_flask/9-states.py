#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<list_id>', strict_slashes=False)
def states_list(list_id=None):
    states = storage.all(State)
    cities = storage.all(City).values()
    if list_id is not None:
        list_id = "State.{}" + list_id
    return render_template('9-states.html', states=states, cities=cities, list_id=list_id)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run()
