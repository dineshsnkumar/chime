from flask import Flask, redirect, url_for, request
from radioastrophysicalobject import RadioPhysicalObject

app = Flask(__name__)

radio_physical_objects = {
    0: {
        "type": "neutron_star",
        "dispersion": 12.0,
        "right_ascension": 2.5,
        "declination": 12,
        "cosmicness": 1

    },
    1: {
        "type": "rrat",
        "dispersion": 12.0,
        "right_ascension": 2.5,
        "declination": 12,
        "cosmicness": 1
    }
}


# Home route
@app.route('/')
def home():
    return redirect(url_for('radioobjects'))


# Returns the list of objects
@app.route('/radioobjects')
def radio_objects():
    return radio_physical_objects


# Add a new object
@app.route('/radioobjects', methods=["POST"])
def add_radio_object():
    data = request.get_json()
    index = len(radio_physical_objects)
    radio_physical_objects[index] = data
    return radio_physical_objects


@app.route('/radioobjects/<string:id>', method=["PUT"])
def change_radio_object():
    pass


@app.route('/radioobjects/<string:id>', method=["DELETE"])
def delete_radio_object():
    pass


app.run(port=5000)
