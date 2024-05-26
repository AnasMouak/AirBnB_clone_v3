#!/usr/bin/python3
"""City-related API endpoints."""
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.state import City
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'],
                 strict_slashes=False)
def sties(state_id):
    """ Retrieves the list of all City objects of a State """

    if request.method == 'GET':
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        cities_list = [city.to_dict() for city in state.cities]
        return jsonify(cities_list)
    elif request.method == 'POST':
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        data = request.get_json()
        if not data:
            abort(400, description="Not a JSON")
        if 'name' not in data:
            abort(400, description="Missing name")

        new_city = City(**data)
        new_city.state_id = state_id
        storage.new(new_city)
        storage.save()

        return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def cities(city_id):
    """ Retrieves a specific City object by ID """
    if request.method == 'GET':
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        return jsonify(city.to_dict())

    elif request.method == 'PUT':
        city = storage.get(City, city_id)
        if city is None:
            abort(404)

        data = request.get_json()
        if not data:
            abort(400, description="Not a JSON")

        ignored_keys = {'id', 'state_id', 'created_at', 'updated_at'}
        for key, value in data.items():
            if key not in ignored_keys:
                setattr(city, key, value)

        storage.save()
        return jsonify(city.to_dict()), 200
    elif request.method == 'DELETE':
        city = storage.get(City, city_id)
        if city is None:
            abort(404)

        storage.delete(city)
        storage.save()
        return jsonify({}), 200
