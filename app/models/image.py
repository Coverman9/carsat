from .db import db, environment, SCHEMA, add_prefix_for_prod


class Image(db.Model):
    __tablename__ = 'images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("cars.id"), ondelete="CASCADE"), nullable=False)
    image = db.Column(db.String)

    car = db.relationship("Car", back_populates="images")

    def to_dict(self):
        return {
            'id': self.id,
            'carId': self.car_id,
            'image': self.image,
            'car': self.car.to_dict_no_ref(),
        }

    def to_dict_no_ref(self):
        return {
            'id': self.id,
            'carId': self.car_id,
            'image': self.image,
        }
