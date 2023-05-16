from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', first_name='Demo', last_name='User', password='password')
    marnie = User(
        username='Marnie', email='marnie@aa.io', first_name='Marnie', last_name='Gonzales', password='password')
    bobbie = User(
        username='Bobbie', email='bobbie@aa.io', first_name='Bobbie', last_name='Smith', password='password')
    lionel = User(
        username='Messi', email='messi@aa.io', first_name='Lionel', last_name='Messi', password='password')
    cristiano = User(
        username='Ronaldo', email='cristina@aa.io', first_name='Cristiano', last_name='Ronaldo', password='password')
    zlatan = User(
        username='Zlatan', email='zlatan@aa.io', first_name='Zlatan', last_name='Ibrahimovic', password='password')
    frank = User(
        username='Franky', email='frank@aa.io', first_name='Frank', last_name='Lampard', password='password')
    sergio = User(
        username='Ramos', email='ramos@aa.io', first_name='Sergio', last_name='Ramos', password='password')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(lionel)
    db.session.add(cristiano)
    db.session.add(zlatan)
    db.session.add(frank)
    db.session.add(sergio)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
