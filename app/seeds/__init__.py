from flask.cli import AppGroup
from .users import seed_users, undo_users
from .cars import seed_cars, undo_cars
from .reviews import seed_reviews, undo_reviews
from .test_drives import seed_testdrives, undo_testdrives
from .wishlists import seed_wishlists, undo_wishlists
from .images import seed_images, undo_images

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_wishlists()
        undo_reviews()
        undo_testdrives()
        undo_images()
        undo_cars()
        undo_users()

    seed_users()
    seed_cars()
    seed_images()
    seed_reviews()
    seed_testdrives()
    seed_wishlists()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_wishlists()
    undo_reviews()
    undo_testdrives()
    undo_images()
    undo_cars()
    undo_users()
    # Add other undo functions here
