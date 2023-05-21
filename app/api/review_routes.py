from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Review, User, Car,db
from ..forms import ReviewForm
from .auth_routes import validation_errors_to_error_messages
from datetime import datetime

review_routes = Blueprint('reviews', __name__)


@review_routes.route('car/<int:id>')
@login_required
def get_all_reviews_of_current_car(id):
    """
    This route gets all reviews that are belongs to car
    """
    reviews = Review.query.filter(Review.car_id == id).all()

    return {'reviews': [review.to_dict() for review in reviews]}


@review_routes.route('user/<int:id>')
@login_required
def get_all_reviews_of_current_user(id):
    """
    This route get all reviews that are belongs to user
    """
    reviews = Review.query.filter(Review.user_id == id).all()

    return {'reviews': [review.to_dict() for review in reviews]}



@review_routes.route('/<int:carId>', methods=['POST'])
@login_required
def create_review(carId):
    """
    This route creates a review for the logged-in user
    """

    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        new_review = Review(
            user = current_user,
            car_id = carId,
            review = form.data['review'],
            stars = form.data['stars']
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review.to_dict()

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@review_routes.route('/<int:id>', methods=['PUT'])  # PATCH too?
@login_required
def update_review(id):
    """
    This route updates review specified by id
    for the logged-in user if that user is the owner
    """

    review_to_update = Review.query.get(id)

    if current_user.id != review_to_update.user_id:
        return {'errors': ['Forbidden']}, 403

    form = ReviewForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        review_to_update.review = form.data['review']
        review_to_update.stars = form.data['stars']


        db.session.commit()
        return review_to_update.to_dict()

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400



@review_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_review(id):
    """
    This route deletes the review specified by id
    if the logged-in user is the owner
    """
    print("DOHODIW")
    review_to_delete = Review.query.get(id)

    if current_user.id != review_to_delete.user_id:
        return {'errors': ['Forbidden']}, 403

    db.session.delete(review_to_delete)

    db.session.commit()

    return {'message': f"Successfully deleted review {review_to_delete}"}
