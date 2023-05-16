from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Testdrive(db.Model):
    __tablename__ = 'testdrives'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("users.id")), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod("cars.id"), ondelete="CASCADE"), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    user = db.relationship("User", back_populates="test_drives")
    car = db.relationship("Car", back_populates="test_drives")

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'carId': self.car_id,
            'startDate': self.start_date,
            'endDate': self.end_date,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'user': self.user.to_dict_no_ref(),
            'message': self.message.to_dict_no_ref()
        }

    def to_dict_no_ref(self):
        return {
            'userId': self.user_id,
            'carId': self.car_id,
            'startDate': self.start_date,
            'endDate': self.end_date,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
        }
