#!/usr/bin/python3
"""place-related API endpoints."""
from flask import abort, jsonify, request
from models import storage
from models.place import Place
from models.state import City
from models.state import State
from models.amenity import Amenity
from models.user import User
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET', 'POST'],
                 strict_slashes=False)
def platies(city_id):
    """ Retrieves the list of all Place objects of a City """

    if request.method == 'GET':
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        places_list = [place.to_dict() for place in city.places]
        return jsonify(places_list)
    elif request.method == 'POST':
        city = storage.get(City, city_id)
        if city is None:
            abort(404)

        data = request.get_json()
        if not data:
            abort(400, description="Not a JSON")
        if 'user_id' not in data:
            abort(400, description="Missing user_id")

        user = storage.get(User, data['user_id'])
        if user is None:
            abort(404)
        if 'name' not in data:
            abort(400, description="Missing name")

        new_place = Place(**data)
        new_place.city_id = city_id
        storage.new(new_place)
        storage.save()

        return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def places(place_id):
    """ Retrieves a specific Place object by ID """
    if request.method == 'GET':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)
        return jsonify(place.to_dict())

    elif request.method == 'PUT':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        data = request.get_json()
        if not data:
            abort(400, description="Not a JSON")

        ignored_keys = {'id', 'user_id', 'city_id', 'created_at', 'updated_at'}
        for key, value in data.items():
            if key not in ignored_keys:
                setattr(place, key, value)

        storage.save()
        return jsonify(place.to_dict()), 200
    elif request.method == 'DELETE':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        storage.delete(place)
        storage.save()
        return jsonify({}), 200


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def places_search():
    """Searches for Place objects based on JSON data"""
    if request.mimetype != 'application/json':
        abort(400, description="Not a JSON")
    data = request.get_json()
    if not data:
        return jsonify([place.to_dict() for place in
                        storage.all(Place).values()])
    states = data.get('states', [])
    cities = data.get('cities', [])
    amenities = data.get('amenities', [])
    if not states and not cities and not amenities:
        return jsonify([place.to_dict() for place in
                        storage.all(Place).values()])
    places = []
    if states:
        states_obj = [storage.get(State, state_id) for state_id in states]
        for state in states_obj:
            if state:
                for city in state.cities:
                    places.extend(city.places)
    if cities:
        city_obj = [storage.get(City, city_id) for city_id in cities]
        for city in city_obj:
            if city:
                places.extend(city.places)
    if amenities:
        if not places:
            places = storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, amenity_id)
                         for amenity_id in amenities]
        places = [place for place in places
                  if all(amenity in place.amenities
                         for amenity in amenities_obj)]
    places = list(set(places))
    return jsonify([place.to_dict() for place in places])
