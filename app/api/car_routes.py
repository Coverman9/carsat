from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Car, User, db
from ..forms import CarForm
from .auth_routes import validation_errors_to_error_messages
from datetime import datetime

car_routes = Blueprint('cars', __name__)


@car_routes.route('')
@login_required
def get_all_cars():
    """
    This route gets all cars that are in the db
    """
    cars = Car.query.all()
    return {'cars': [car.to_dict() for car in cars]}


@car_routes.route('/<int:id>')
@login_required
def get_one_car(id):
    """
    This route get one car by car_id
    """
    car = Car.query.get(id)
    if car:
        return {'car': car.to_dict()}
    return {'errors': ["Not Found"]}, 404


@car_routes.route('', methods=['POST'])
@login_required
def create_car():
    """
    This route creates a car for the logged-in user
    """

    form = CarForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        car = Car(
            make=form.data['make'],
            model=form.data['model'],
            type=form.data['type'],
            year=form.data['year'],
            mileage=form.data['mileage'],
            price=form.data['price'],
            color=form.data['color'],
            car_description=form.data['car_description'],
            owner=current_user,
            created_at = datetime.now()
        )
        print("CAR", car)
        db.session.add(car)
        db.session.commit()
        return car.to_dict()

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@car_routes.route('/<int:id>', methods=['PUT'])  # PATCH too?
@login_required
def update_car(id):
    """
    This route updates info of the car specified by id
    for the logged-in user if that user is the owner
    """

    car_to_update = Car.query.get(id)

    if current_user.id != car_to_update.owner_id:
        return {'errors': ['Forbidden']}, 403

    form = CarForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        car_to_update.make = form.data['make']
        car_to_update.model = form.data['model']
        car_to_update.type = form.data['type']
        car_to_update.year = form.data['year']
        car_to_update.mileage = form.data['mileage']
        car_to_update.price = form.data['price']
        car_to_update.color = form.data['color']
        car_to_update.car_description = form.data['car_description']

        db.session.commit()
        return {'car': car_to_update.to_dict()}

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400



@car_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_ar(id):
    """
    This route deletes the car specified by id
    if the logged-in user is the owner
    """

    car_to_delete = Car.query.get(id)

    if current_user.id != car_to_delete.owner_id:
        return {'errors': ['Forbidden']}, 403

    db.session.delete(car_to_delete)

    db.session.commit()

    return {'message': f"Successfully deleted car {car_to_delete}"}
