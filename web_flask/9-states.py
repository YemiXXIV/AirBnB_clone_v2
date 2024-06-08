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


@app.route("/states")
def states_list():
    """
    List all states
    """
    Data = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("9-states.html", states=Data)


@app.route("/states/<id>")
def states_by_id(id):
    """
    List all cities in state with id
    """
    try:
        state = list(filter(lambda x: id == x.id,
                            storage.all(State).values()))[0]
        heading = "State: " + state.name
        cities = state.cities
        return render_template(
            "9-states.html", state=state,
            cities=cities, heading=heading
        )
    except IndexError:
        return render_template(
            "9-states.html", state=None,
            cities=None, heading="Not found!"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
