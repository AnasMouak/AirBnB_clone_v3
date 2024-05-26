#!/usr/bin/python3
"""Amenity-related API endpoints."""
from flask import jsonify, abort, request
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET', 'POST'], strict_slashes=False)
@app_views.route('/amenities/<amenity_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def amenities(amenity_id=None):
    """ Retrieves the list of all Amenity objects """
    if amenity_id is None:
        if request.method == 'GET':
            amenities_list = [amenity.to_dict() for amenity in
                              storage.all(Amenity).values()]
            return jsonify(amenities_list)
        elif request.method == 'POST':
            data = request.get_json()
            if not data:
                abort(400, description="Not a JSON")
            if 'name' not in data:
                abort(400, description="Missing name")

            new_amenity = Amenity(**data)
            storage.new(new_amenity)
            storage.save()

            return jsonify(new_amenity.to_dict()), 201

    elif amenity_id:
        if request.method == 'GET':
            amenity = storage.get(Amenity, amenity_id)
            if amenity is None:
                abort(404)
            return jsonify(amenity.to_dict())
        elif request.method == 'PUT':
            amenity = storage.get(Amenity, amenity_id)
            if amenity is None:
                abort(404)

            data = request.get_json()
            if not data:
                abort(400, description="Not a JSON")

            ignored_keys = {'id', 'created_at', 'updated_at'}
            for key, value in data.items():
                if key not in ignored_keys:
                    setattr(amenity, key, value)

            storage.save()
            return jsonify(amenity.to_dict()), 200
        elif request.method == 'DELETE':
            amenity = storage.get(Amenity, amenity_id)
            if amenity is None:
                abort(404)

            storage.delete(amenity)
            storage.save()
            return jsonify({}), 200
