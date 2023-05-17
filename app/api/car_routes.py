from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Car, User, db
from ..forms import CarForm
from .auth_routes import validation_errors_to_error_messages

car_routes = Blueprint('cars', __name__)


@car_routes.route('')
@login_required
def get_all_channels():
    """
    This route gets all channels that are in the db
    """
    channels = Channel.query.all()
    return {'channels': [channel.to_dict() for channel in channels]}


@car_routes.route('/<int:id>')
@login_required
def get_one_channel(id):
    """
    This route get one channel by channel_id
    """
    channel = Channel.query.get(id)
    if channel:
        return {'channel': channel.to_dict()}
    return {'errors': ["Not Found"]}, 404


def can_create(current_members_ids, all_channel_members):
            if len(current_members_ids) != len(all_channel_members):
                return True
            for id in current_members_ids:
                all_channel_members_ids = [member.id for member in all_channel_members]
                if id not in all_channel_members_ids:
                    return True
            return False

@car_routes.route('', methods=['POST'])
@login_required
def create_channel():
    """
    This route creates a channel for the logged-in user
    """

    form = ChannelForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        channel = Channel(
            channel_name=form.data['channelName'],
            description=form.data['description'],
            is_dm=form.data['isDm'],
            owner=current_user
        )


        channel.members.append(current_user)

        addUsers = request.get_json()['addUsers']

        # Check for Uniquness if channel is a DM
        if channel.is_dm:
            all_channels = Channel.query.filter(Channel.is_dm).all()
            # print(f"GETTING ALL CHANNELS ---------------> : {all_channels}")

            current_dm_users = [*addUsers, current_user.id]

            able_to_create = True

            for channel in all_channels:
                # print("current_dm_users ----> ", current_dm_users)
                # print("channel.members ----> ", channel.members)

                if not can_create(current_dm_users, channel.members):
                    able_to_create = False
                    break

            print("ARE WE ABLE TO CREATE? ----> ", able_to_create)
            if not able_to_create:
                print("INSIDE IF NOT ABLE TO CREATE ")
                return {'errors': ["Dm already exists"]}, 400


        users_to_add = User.query.filter(User.id.in_(addUsers)).all()

        [channel.members.append(user) for user in users_to_add]

        db.session.add(channel)
        db.session.commit()
        return {'channel': channel.to_dict()}

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400


@car_routes.route('/<int:id>', methods=['PUT'])  # PATCH too?
@login_required
def update_channel(id):
    """
    This route updates the name and description of the channel specified by id
    for the logged-in user if that user is the owner
    """

    channel_to_update = Channel.query.get(id)

    if current_user.id != channel_to_update.owner_id:
        return {'errors': ['Forbidden']}, 403

    form = ChannelForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():

        channel_to_update.channel_name = form.data['channelName']
        channel_to_update.description = form.data['description']

        db.session.commit()
        return {'channel': channel_to_update.to_dict()}

    # or 422
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400



@car_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_channel(id):
    """
    This route deletes the channel specified by id
    if the logged-in user is the owner
    """

    channel_to_delete = Channel.query.get(id)

    channel_to_delete_name = channel_to_delete.channel_name

    if current_user.id != channel_to_delete.owner_id:
        return {'errors': ['Forbidden']}, 403

    db.session.delete(channel_to_delete)

    db.session.commit()

    return {'message': f"Successfully deleted channel {channel_to_delete_name}"}
