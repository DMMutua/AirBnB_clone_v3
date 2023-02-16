#!/usr/bin/python3
"""Index of the API blueprint"""


import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """Function that returns the Status of the API"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def object_stats():
    """Retrieval of Object Number Stats by Type. Displays jsonified content"""


    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User
    from models import storage


    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities","cities","places","reviews","states","users"]

    no_objs = {}
    for i in range(len(classes)):
        no_objs[names[i]] = storage.count(classes[i])

    return jsonify(no_objs)
