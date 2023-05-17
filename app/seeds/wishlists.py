from app.models import db, Wishlist, environment, SCHEMA
from sqlalchemy.sql import text


def seed_wishlists():
    wishlist = Wishlist(
        user_id=1,
        car_id=2,
        description='One day this car will be mine',
    )
    wishlist2 = Wishlist(
        user_id=2,
        car_id=12,
        description='One day this car will be mine',
    )
    wishlist3 = Wishlist(
        user_id=3,
        car_id=9,
        description='One day this car will be mine',
    )
    wishlist4 = Wishlist(
        user_id=4,
        car_id=14,
        description='One day this car will be mine',
    )
    wishlist5 = Wishlist(
        user_id=5,
        car_id=17,
        description='One day this car will be mine',
    )
    wishlist6 = Wishlist(
        user_id=6,
        car_id=18,
        description='One day this car will be mine',
    )
    wishlist7 = Wishlist(
        user_id=7,
        car_id=3,
        description='One day this car will be mine',
    )
    wishlist8 = Wishlist(
        user_id=8,
        car_id=4,
        description='One day this car will be mine',
    )
    wishlist9 = Wishlist(
        user_id=1,
        car_id=9,
        description='One day this car will be mine',
    )


    all_wishlists = [wishlist, wishlist2, wishlist3, wishlist4, wishlist5, wishlist6,
                   wishlist7, wishlist8, wishlist9]
    add_wishlists = [db.session.add(wishlist) for wishlist in all_wishlists]
    db.session.commit()
    print('all wishlists added')


def undo_wishlists():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.wishlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM wishlists"))

    db.session.commit()
