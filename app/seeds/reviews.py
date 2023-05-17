from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text


def seed_reviews():
    review = Review(
        user_id=8,
        car_id=2,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review1 = Review(
        user_id=1,
        car_id=3,
        review='Used to drive this car, its really cool',
        stars=4
    )
    review2 = Review(
        user_id=1,
        car_id=4,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review3 = Review(
        user_id=2,
        car_id=5,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review4 = Review(
        user_id=2,
        car_id=6,
        review='Used to drive this car, its really cool',
        stars=4
    )
    review5 = Review(
        user_id=8,
        car_id=7,
        review='Used to drive this car, its really cool',
        stars=3
    )
    review = Review(
        user_id=3,
        car_id=8,
        review='Used to drive this car, its really cool',
        stars=4
    )
    review6 = Review(
        user_id=3,
        car_id=9,
        review='Used to drive this car, its really cool',
        stars=4
    )
    review7 = Review(
        user_id=8,
        car_id=1,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review8 = Review(
        user_id=3,
        car_id=2,
        review='Used to drive this car, its really cool',
        stars=3
    )
    review9 = Review(
        user_id=4,
        car_id=3,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review10 = Review(
        user_id=4,
        car_id=4,
        review='Used to drive this car, its really cool',
        stars=3
    )
    review11 = Review(
        user_id=1,
        car_id=5,
        review='Used to drive this car, its really cool',
        stars=4
    )
    review12 = Review(
        user_id=5,
        car_id=6,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review13 = Review(
        user_id=5,
        car_id=7,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review14 = Review(
        user_id=5,
        car_id=8,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review15 = Review(
        user_id=6,
        car_id=9,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review16 = Review(
        user_id=6,
        car_id=1,
        review='Used to drive this car, its really cool',
        stars=4
    )
    review17 = Review(
        user_id=6,
        car_id=11,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review18 = Review(
        user_id=7,
        car_id=11,
        review='Used to drive this car, its really cool',
        stars=5
    )
    review19 = Review(
        user_id=7,
        car_id=13,
        review='Used to drive this car, its really cool',
        stars=5
    )

    all_reviews = [review, review2, review3, review4, review5, review6,
                   review7, review8, review9, review10, review11, review12,
                   review13, review14, review15, review16, review17, review18,
                   review19]
    add_reviews = [db.session.add(review) for review in all_reviews]
    db.session.commit()
    print('all reviews added')


def undo_reviews():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
