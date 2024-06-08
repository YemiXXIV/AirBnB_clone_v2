#!/usr/bin/python3
""" A route to /states_list """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exception):
    """ Teardown method """
    storage.close()


@app.route('/hbnb')
def hbnb():
    """ Route to /hbnb_filters """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities,
                           places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
