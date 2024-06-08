#!/usr/bin/python3
""" A route to /states_list """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exception):
    storage.close()


@app.route("/cities_by_states")
def cities_by_states():
    """A route to /cities_by_states"""
    data = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
