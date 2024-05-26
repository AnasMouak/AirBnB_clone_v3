#!/usr/bin/python3
"""User-related API endpoints."""
from flask import jsonify, abort, request
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
@app_views.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def users(user_id=None):
    """ Retrieves the list of all User objects """
    if user_id is None:
        if request.method == 'GET':
            users_list = [user.to_dict() for user in
                          storage.all(User).values()]
            return jsonify(users_list)
        elif request.method == 'POST':
            data = request.get_json()
            if not data:
                abort(400, description="Not a JSON")
            if 'email' not in data:
                abort(400, description="Missing email")
            if 'password' not in data:
                abort(400, description="Missing password")

            new_user = User(**data)
            storage.new(new_user)
            storage.save()

            return jsonify(new_user.to_dict()), 201

    elif user_id:
        if request.method == 'GET':
            user = storage.get(User, user_id)
            if user is None:
                abort(404)
            return jsonify(user.to_dict())
        elif request.method == 'PUT':
            user = storage.get(User, user_id)
            if user is None:
                abort(404)

            data = request.get_json()
            if not data:
                abort(400, description="Not a JSON")

            ignored_keys = {'id', 'email', 'created_at', 'updated_at'}
            for key, value in data.items():
                if key not in ignored_keys:
                    setattr(user, key, value)

            storage.save()
            return jsonify(user.to_dict()), 200
        elif request.method == 'DELETE':
            user = storage.get(User, user_id)
            if user is None:
                abort(404)

            storage.delete(user)
            storage.save()
            return jsonify({}), 200
