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
