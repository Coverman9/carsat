from .db import db, environment, SCHEMA, add_prefix_for_prod

class Car(db.Model):
    __tablename__ = 'cars'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    mileage = db.Column(db.Integer, default='New')
    price = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    car_description = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, nullable=False)


    owner = db.relationship("User", back_populates="cars")
    reviews = db.relationship("Review", back_populates="car")
    images = db.relationship("Image", back_populates="car")
    wishlists = db.relationship("Wishlist", back_populates="car")
    test_drives = db.relationship("Testdrive", back_populates="car")

    def to_dict(self):
        realOwner = self.owner.to_dict_no_ref() if self.owner is not None else None
        return {
            'id': self.id,
            'ownerId': self.owner_id,
            'make': self.make,
            'model': self.model,
            'type': self.type,
            'year': self.year,
            'mileage': self.mileage,
            'price': self.price,
            'color': self.color,
            'carDescription': self.car_description,
            'createdAt': self.created_at,
            'owner': realOwner,
            'reviews': [review.to_dict_no_ref() for review in self.reviews],
            'images': [image.to_dict_no_ref() for image in self.images],
            'wishlists': [wishlist.to_dict_no_ref() for wishlist in self.wishlists],
            'testDrives': [test_drive.to_dict_no_ref() for test_drive in self.test_drives],

        }

    def to_dict_no_ref(self):
        return {
           'id': self.id,
            'ownerId': self.owner_id,
            'make': self.make,
            'model': self.model,
            'type': self.type,
            'year': self.year,
            'mileage': self.mileage,
            'price': self.price,
            'color': self.color,
            'carDescription': self.car_description,
            'createdAt': self.created_at,
        }
