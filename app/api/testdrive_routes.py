from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Testdrive, User, Car,db
from ..forms import TestdriveForm
from .auth_routes import validation_errors_to_error_messages
from datetime import datetime

testdrive_routes = Blueprint('testdrives', __name__)


@testdrive_routes.route('car/<int:id>')
@login_required
def get_all_testdrives_for_current_car(id):
    """
    This route gets all testdrives that are belongs to car
    """
    testdrives = Testdrive.query.filter(Testdrive.car_id == id).all()

    return {'testdrives': [testdrive.to_dict() for testdrive in testdrives]}


@testdrive_routes.route('user/<int:id>')
@login_required
def get_all_testdrves_of_current_user(id):
    """
    This route get all testdrives that are belongs to user
    """
    testdrives = Testdrive.query.filter(Testdrive.user_id == id).all()

    return {'testdrives': [testdrive.to_dict() for testdrive in testdrives]}



@testdrive_routes.route('/<int:carId>', methods=['POST'])
@login_required
def create_testdrive(carId):
    """
    This route creates testdrive for the logged-in user
    """

    form = TestdriveForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        new_testdrive = Testdrive(
            user = current_user,
            car_id = carId,
            testdrive_date = form.data['testdrive_date'],
        )
        db.session.add(new_testdrive)
        db.session.commit()
        return new_testdrive.to_dict()

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@testdrive_routes.route('/<int:id>', methods=['PUT'])  # PATCH too?
@login_required
def update_testdrive(id):
    """
    This route updates testdrive date specified by id
    for the logged-in user if that user is the owner
    """

    testdrive_to_update = Testdrive.query.get(id)

    if current_user.id != testdrive_to_update.user_id:
        return {'errors': ['Forbidden']}, 403

    form = TestdriveForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        testdrive_to_update.testdrive_date = form.data['testdrive_date']


        db.session.commit()
        return testdrive_to_update.to_dict()

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400



@testdrive_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def cancel_testdrive(id):
    """
    This route cancels testdrive specified by id
    if the logged-in user is the owner
    """
    testdrive_to_delete = Testdrive.query.get(id)

    if current_user.id != testdrive_to_delete.user_id:
        return {'errors': ['Forbidden']}, 403

    db.session.delete(testdrive_to_delete)

    db.session.commit()

    return {'message': f"Successfully deleted review {testdrive_to_delete}"}
