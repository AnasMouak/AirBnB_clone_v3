#!/usr/bin/python3
"""place_reviews-related API endpoints."""
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.user import User
from models.review import Review
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'],
                 strict_slashes=False)
def plawies(place_id):
    """ Retrieves the list of all Review objects of a Place """

    if request.method == 'GET':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)
        reviews_list = [review.to_dict() for review in place.reviews]
        return jsonify(reviews_list)
    elif request.method == 'POST':
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)

        data = request.get_json()
        if not data:
            abort(400, description="Not a JSON")
        if 'user_id' not in data:
            abort(400, description="Missing user_id")

        user = storage.get(User, data['user_id'])
        if user is None:
            abort(404)
        if 'text' not in data:
            abort(400, description="Missing text")

        new_review = Review(**data)
        new_review.place_id = place_id
        storage.new(new_review)
        storage.save()

        return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'],
                 strict_slashes=False)
def reviews(review_id):
    """ Retrieves a specific Review object by ID """
    if request.method == 'GET':
        review = storage.get(Review, review_id)
        if review is None:
            abort(404)
        return jsonify(review.to_dict())

    elif request.method == 'PUT':
        review = storage.get(Review, review_id)
        if review is None:
            abort(404)

        data = request.get_json()
        if not data:
            abort(400, description="Not a JSON")

        ignored_keys = {'id', 'user_id', 'place_id', 'created_at',
                        'updated_at'}
        for key, value in data.items():
            if key not in ignored_keys:
                setattr(review, key, value)

        storage.save()
        return jsonify(review.to_dict()), 200
    elif request.method == 'DELETE':
        review = storage.get(Review, review_id)
        if review is None:
            abort(404)

        storage.delete(review)
        storage.save()
        return jsonify({}), 200
