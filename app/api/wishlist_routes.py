from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Wishlist, User, Car,db
from ..forms import WishlistForm
from .auth_routes import validation_errors_to_error_messages
from datetime import datetime

wishlist_routes = Blueprint('wishlists', __name__)


@wishlist_routes.route('car/<int:id>')
@login_required
def get_all_wishlists_of_current_car(id):
    """
    This route gets all wishlists that are belongs to car
    """
    wishlists = Wishlist.query.filter(Wishlist.car_id == id).all()

    return {'wishlists': [wishlist.to_dict() for wishlist in wishlists]}


@wishlist_routes.route('user/<int:id>')
@login_required
def get_all_wishlists_of_current_user(id):
    """
    This route get all wishlists that are belongs to user
    """
    wishlists = Wishlist.query.filter(Wishlist.user_id == id).all()

    return {'wishlists': [wishlist.to_dict() for wishlist in wishlists]}



@wishlist_routes.route('/<int:carId>', methods=['POST'])
@login_required
def add_to_wishlist(carId):
    """
    This route add a car to the wishlist for the logged-in user
    """

    form = WishlistForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        new_wish = Wishlist(
            user = current_user,
            car_id = carId,
            description = form.data['description']
        )
        db.session.add(new_wish)
        db.session.commit()
        return new_wish.to_dict()

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@wishlist_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def remove_from_wishlist(id):
    """
    This route deletes the wishlist specified by id
    if the logged-in user is the owner
    """
    wishlists_to_delete = Wishlist.query.get(id)

    if current_user.id != wishlists_to_delete.user_id:
        return {'errors': ['Forbidden']}, 403

    db.session.delete(wishlists_to_delete)

    db.session.commit()

    return {'message': f"Successfully deleted wishlist {wishlists_to_delete}"}
