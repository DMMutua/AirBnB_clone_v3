#!/usr/bin/python3
"""Index of the API blueprint"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False, methods=['GET'])
def status():
    """Function that returns the Status of the API"""
    return jsonify({"status": "OK"})
