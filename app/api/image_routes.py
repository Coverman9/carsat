from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Image, User, Car, db
from ..forms import ImageForm
from .auth_routes import validation_errors_to_error_messages
from datetime import datetime
from .aws_helpers import upload_file_to_s3, get_unique_filename

image_routes = Blueprint('images', __name__)


@image_routes.route('')
@login_required
def get_all_images_of_current_car():
    """
    This route gets all images that are belongs to car
    """
    images = Image.query.all()

    return [image.to_dict() for image in images]


@image_routes.route('/<int:carId>', methods=['POST'])
@login_required
def upload_image(carId):
    """
    This route add a car to the wishlist for the logged-in user
    """

    form = ImageForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        image = form.data['image']
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)

        if 'url' not in upload:
            return {'errors': ['Image wasnt upload']}, 403

        new_image = Image(
            car_id = carId,
            image = upload["url"]
        )
        db.session.add(new_image)
        db.session.commit()
        return new_image.to_dict()

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@image_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def remove_image(id):
    """
    This route deletes the wishlist specified by id
    if the logged-in user is the owner
    """
    image_to_remove = Image.query.get(id)

    if current_user.id != image_to_remove.user_id:
        return {'errors': ['Forbidden']}, 403

    db.session.delete(image_to_remove)

    db.session.commit()

    return {'message': f"Successfully deleted image {image_to_remove}"}
