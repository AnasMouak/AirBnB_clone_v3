#!/usr/bin/python3
"""State-related API endpoints."""
from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def states(state_id=None):
    """ Retrieves the list of all State objects """
    if state_id is None:
        if request.method == 'GET':
            states_list = [state.to_dict() for state in
                           storage.all(State).values()]
            return jsonify(states_list)
        elif request.method == 'POST':
            data = request.get_json()
            if not data:
                abort(400, description="Not a JSON")
            if 'name' not in data:
                abort(400, description="Missing name")

            new_state = State(**data)
            storage.new(new_state)
            storage.save()

            return jsonify(new_state.to_dict()), 201

    elif state_id:
        if request.method == 'GET':
            state = storage.get(State, state_id)
            if state is None:
                abort(404)
            return jsonify(state.to_dict())
        elif request.method == 'PUT':
            state = storage.get(State, state_id)
            if state is None:
                abort(404)

            data = request.get_json()
            if not data:
                abort(400, description="Not a JSON")

            ignored_keys = {'id', 'created_at', 'updated_at'}
            for key, value in data.items():
                if key not in ignored_keys:
                    setattr(state, key, value)

            storage.save()
            return jsonify(state.to_dict()), 200
        elif request.method == 'DELETE':
            state = storage.get(State, state_id)
            if state is None:
                abort(404)

            storage.delete(state)
            storage.save()
            return jsonify({}), 200
