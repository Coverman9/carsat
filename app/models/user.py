from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)

    cars = db.relationship("Car", back_populates="owner")
    reviews = db.relationship("Review", back_populates="user")
    test_drives = db.relationship("Testdrive", back_populates="user")
    wishlists = db.relationship("Wishlist", back_populates="user")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'cars': [car.to_dict_no_ref() for car in self.cars],
            'reviews': [review.to_dict_no_ref() for review in self.reviews],
            'testDrives': [test_drive.to_dict_no_ref() for test_drive in self.test_drives],
            'wishlists': [wishlist.to_dict_no_ref() for wishlist in self.wishlists]
        }

    def to_dict_no_ref(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'firstName': self.first_name,
            'lastName': self.last_name
        }
