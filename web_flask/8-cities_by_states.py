#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run()
