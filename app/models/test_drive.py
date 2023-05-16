from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Testdrive(db.Model):
    __tablename__ = 'testdrives'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("cars.id"), ondelete="CASCADE"), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    user = db.relationship("User", back_populates="test_drive")
    car = db.relationship("Car", back_populates="test_drive")

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'messageId': self.message_id,
            'reaction': self.reaction,
            'user': self.user.to_dict_no_ref(),
            'message': self.message.to_dict_no_ref()
        }

    def to_dict_no_ref(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'messageId': self.message_id,
            'reaction': self.reaction
        }
