#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    print(states)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(self):
    storage.close()


if __name__ == '__main__':
    app.run()