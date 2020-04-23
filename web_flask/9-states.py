#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<list_id>', strict_slashes=False)
def states_list(list_id=None):
    if list_id is not None:
        states = storage.all(State)
        list_id = "State.{}".format(list_id)
    else:
        states = list(storage.all(State).values())
    return render_template('9-states.html', states=states, list_id=list_id)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run()
