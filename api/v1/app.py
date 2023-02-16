#!/usr/bin/python3
"""The Foundation Implementation of the AirBnB_Clone API.
"""


from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from models import storage
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_storage(exception):
    """Closes Database and Other Persistent Storage Amenities"""
    storage.close()

@app.errorhandler(404)
def res_not_found(error):
    """404 Error Response Output"""
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    """Import Guard; main function"""
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')

    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
