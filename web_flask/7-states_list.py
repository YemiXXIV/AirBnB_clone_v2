#!/usr/bin/python3
""" A route to /states_list """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exception):
    """ Tear down the database again """
    storage.close()


@app.route("/states_list")
def states_list():
    """A route to /states_list"""
    data = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
