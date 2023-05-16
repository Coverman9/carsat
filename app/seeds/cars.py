from app.models import db, Car, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_cars():
    car1 = Car(
        owner_id=1,
        message='Snack time!',
        created_at=datetime.now()
    )


    all_cars = [car1]
    add_cars = [db.session.add(car) for car in all_cars]
    db.session.commit()
    print('all cars added')

def undo_messages():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cars RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cars"))

    db.session.commit()
