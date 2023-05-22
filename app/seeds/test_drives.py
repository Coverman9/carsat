from app.models import db, Testdrive, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_testdrives():
    testdrive = Testdrive(
        user_id=1,
        car_id=2,
        testdrive_date=datetime(2023, 6, 23),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive2 = Testdrive(
        user_id=2,
        car_id=12,
        testdrive_date=datetime(2023, 6, 12),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive3 = Testdrive(
        user_id=3,
        car_id=9,
        testdrive_date=datetime(2023, 6, 4),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive4 = Testdrive(
        user_id=4,
        car_id=14,
        testdrive_date=datetime(2023, 7, 23),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive5 = Testdrive(
        user_id=5,
        car_id=17,
        testdrive_date=datetime(2023, 8, 23),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive6 = Testdrive(
        user_id=6,
        car_id=18,
        testdrive_date=datetime(2023, 6, 13),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive7 = Testdrive(
        user_id=7,
        car_id=3,
        testdrive_date=datetime(2023, 10, 13),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    testdrive8 = Testdrive(
        user_id=8,
        car_id=4,
        testdrive_date=datetime(2023, 9, 27),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    all_testdrives = [testdrive, testdrive2, testdrive3, testdrive4,
                      testdrive5, testdrive6, testdrive7, testdrive8]
    add_testdrives = [db.session.add(testdrive) for testdrive in all_testdrives]
    db.session.commit()
    print('all testdrives added')


def undo_testdrives():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.testdrives RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM testdrives"))

    db.session.commit()
