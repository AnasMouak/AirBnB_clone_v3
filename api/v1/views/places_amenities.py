#!/usr/bin/python3
"""place_amenities-related API endpoints."""
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/places/<place_id>/amenities', methods=['GET'],
                 strict_slashes=False)
def platties(place_id):
    """ Retrieves the list of all Amenity objects of a Place """

    if request.method == 'GET':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)
        amenities_list = [amenity.to_dict() for amenity in place.amenities]
        return jsonify(amenities_list)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST', 'DELETE'], strict_slashes=False)
def iews(place_id, amenity_id):
    """ Link a specific Amenity object by ID """

    if request.method == 'POST':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        amenity = storage.get(Amenity, amenity_id)
        if amenity is None:
            abort(404)

        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200

        place.amenities.append(amenity)
        storage.save()

        return jsonify(amenity.to_dict()), 201

    elif request.method == 'DELETE':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        amenity = storage.get(Amenity, amenity_id)
        if amenity is None or amenity not in place.amenities:
            abort(404)

        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
