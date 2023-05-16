from .db import db, environment, SCHEMA, add_prefix_for_prod


class Wishlist(db.Model):
    __tablename__ = 'wishlists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("cars.id"), ondelete="CASCADE"), nullable=False)
    description = db.Column(db.String, nullable=False)

    user = db.relationship("User", back_populates="wishlists")
    car = db.relationship("Car", back_populates="wishlists")

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'carId': self.car_id,
            'description': self.description,
            'user': self.user.to_dict_no_ref(),
            'car': self.car.to_dict_no_ref()
        }

    def to_dict_no_ref(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'carId': self.car_id,
            'description': self.description
        }
