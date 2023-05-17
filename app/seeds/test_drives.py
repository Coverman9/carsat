from app.models import db, Testdrive, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_testdrives():
    testdrive = Testdrive(
        user_id=1,
        car_id=2,
        start_date=datetime(2023, 6, 23),
        end_date=datetime(2023, 6, 24),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive2 = Testdrive(
        user_id=2,
        car_id=12,
        start_date=datetime(2023, 6, 12),
        end_date=datetime(2023, 6, 14),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive3 = Testdrive(
        user_id=3,
        car_id=9,
        start_date=datetime(2023, 6, 4),
        end_date=datetime(2023, 6, 5),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive4 = Testdrive(
        user_id=4,
        car_id=14,
        start_date=datetime(2023, 7, 23),
        end_date=datetime(2023, 7, 25),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive5 = Testdrive(
        user_id=5,
        car_id=17,
        start_date=datetime(2023, 8, 23),
        end_date=datetime(2023, 8, 26),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive6 = Testdrive(
        user_id=6,
        car_id=18,
        start_date=datetime(2023, 6, 13),
        end_date=datetime(2023, 6, 14),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive7 = Testdrive(
        user_id=7,
        car_id=3,
        start_date=datetime(2023, 10, 13),
        end_date=datetime(2023, 10, 25),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive8 = Testdrive(
        user_id=8,
        car_id=4,
        start_date=datetime(2023, 9, 27),
        end_date=datetime(2023, 9, 29),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    all_testdrives = [testdrive, testdrive2, testdrive3, testdrive4,
                      testdrive5, testdrive6, testdrive7, testdrive8]
    add_testdrives = [db.session.add(testdrive) for testdrive in all_testdrives]
    db.session.commit()
    print('all wishlists added')


def undo_testdrives():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.testdrives RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM testdrives"))

    db.session.commit()
