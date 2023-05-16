from .db import db, environment, SCHEMA, add_prefix_for_prod


class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("cars.id"), ondelete="CASCADE"), nullable=False)
    review = db.Column(db.String, nullable=False)
    stars = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", back_populates="reviews")
    car = db.relationship("Car", back_populates="reviews")

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'carId': self.car_id,
            'review': self.review,
            'stars': self.stars,
            'user': self.user.to_dict_no_ref(),
            'car': self.car.to_dict_no_ref()
        }

    def to_dict_no_ref(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'carId': self.car_id,
            'review': self.review,
            'stars': self.stars,
        }
