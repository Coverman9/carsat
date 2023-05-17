from app.models import db, Car, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_cars():
    car1 = Car(
        owner_id=1,
        make='Chevrolet',
        model='Camaro',
        type='coupe',
        year=2018,
        mileage=123000,
        price=24500,
        color='yellow',
        car_description='Yellow Chevrolet Camaro',
        created_at=datetime.now()
    )
    car2 = Car(
        owner_id=2,
        make='Mercedes',
        model='E Class',
        type='business',
        year=2020,
        mileage=12000,
        price=54500,
        color='black',
        car_description='Black Mercedes E class',
        created_at=datetime.now()
    )
    car3 = Car(
        owner_id=3,
        make='BMW',
        model='5 Series',
        type='business',
        year=2021,
        mileage=7000,
        price=56000,
        color='black',
        car_description='Black BMW 5 series',
        created_at=datetime.now()
    )
    car4 = Car(
        owner_id=4,
        make='Mercedes',
        model='CLS Class',
        type='business',
        year=2019,
        mileage=35000,
        price=47000,
        color='black',
        car_description='Black Mercedes CLS class',
        created_at=datetime.now()
    )
    car5 = Car(
        owner_id=5,
        make='Ford',
        model='Mustang',
        type='cabrio',
        year=2018,
        mileage=79000,
        price=21500,
        color='black',
        car_description='Black Ford Mustang',
        created_at=datetime.now()
    )
    car6 = Car(
        owner_id=6,
        make='Ferrari',
        model='F8 Spyder',
        type='cabrio',
        year=2022,
        mileage=3000,
        price=345000,
        color='red',
        car_description='Red Ferrari F8 Spyder',
        created_at=datetime.now()
    )
    car7 = Car(
         owner_id=3,
        make='Chevrolet',
        model='Corvette',
        type='cabrio',
        year=2018,
        mileage=62000,
        price=67000,
        color='yellow',
        car_description='Yellow Chevrolet Corvette',
        created_at=datetime.now()
    )
    car8 = Car(
        owner_id=8,
        make='Rolls Royce',
        model='Wraith',
        type='coupe',
        year=2020,
        mileage=15000,
        price=520000,
        color='black',
        car_description='Black Rolls Royce Wraith',
        created_at=datetime.now()
    )
    car9 = Car(
        owner_id=7,
        make='BMW',
        model='4 Series',
        type='coupe',
        year=2018,
        mileage=123000,
        price=24500,
        color='yellow',
        car_description='Black Chevrolet Camaro',
        created_at=datetime.now()
    )
    car10 = Car(
        owner_id=2,
        make='Porsche',
        model='911',
        type='coupe',
        year=2020,
        mileage=34000,
        price=145000,
        color='white',
        car_description='White Porsche 911',
        created_at=datetime.now()
    )
    car11 = Car(
        owner_id=3,
        make='Mercedes',
        model='AMG GT',
        type='sportcar',
        year=2021,
        mileage=46000,
        price=245000,
        color='gray',
        car_description='Gray Mercedes AMG GT',
        created_at=datetime.now()
    )
    car12 = Car(
        owner_id=4,
        make='BMW',
        model='M8',
        type='sportcar',
        year=2020,
        mileage=87000,
        price=180000,
        color='gray',
        car_description='Gray BMW M8',
        created_at=datetime.now()
    )
    car13 = Car(
        owner_id=5,
        make='Lamborghini',
        model='Huracan',
        type='sportcar',
        year=2021,
        mileage=14000,
        price=295000,
        color='blue',
        car_description='Blue Lamborghini Huracan',
        created_at=datetime.now()
    )
    car14 = Car(
        owner_id=6,
        make='BMW',
        model='X7',
        type='SUV',
        year=2020,
        mileage=74000,
        price=12000,
        color='black',
        car_description='Black BMW X7',
        created_at=datetime.now()
    )
    car15 = Car(
        owner_id=7,
        make='Mercedes',
        model='G Class',
        type='SUV',
        year=2017,
        mileage=167000,
        price=89000,
        color='black',
        car_description='Black Mercedes G Class',
        created_at=datetime.now()
    )
    car16 = Car(
        owner_id=8,
        make='Lamborghini',
        model='Urus',
        type='SUV',
        year=2020,
        mileage=23000,
        price=245000,
        color='black',
        car_description='Black Lamborghini Urus',
        created_at=datetime.now()
    )
    car17 = Car(
        owner_id=1,
        make='Mercedes',
        model='V Class',
        type='van',
        year=2016,
        mileage=240000,
        price=45000,
        color='black',
        car_description='Black Mercedes V Class',
        created_at=datetime.now()
    )
    car18 = Car(
        owner_id=2,
        make='KIA',
        model='Carnival',
        type='van',
        year=2021,
        mileage=152000,
        price=65000,
        color='white',
        car_description='White KIA Carnival',
        created_at=datetime.now()
    )
    car19 = Car(
        owner_id=3,
        make='Toyota',
        model='Alphard',
        type='van',
        year=2019,
        mileage=114000,
        price=48000,
        color='black',
        car_description='Black Toyota Alphard',
        created_at=datetime.now()
    )
    car20 = Car(
        owner_id=4,
        make='Audi',
        model='A5',
        type='business',
        year=2020,
        mileage=34000,
        price=57000,
        color='green',
        car_description='Green Audi A5',
        created_at=datetime.now()
    )
    car21 = Car(
        owner_id=5,
        make='Dodge',
        model='Challenger',
        type='coupe',
        year=2020,
        mileage=123000,
        price=34000,
        color='black',
        car_description='Black Dodge Challenger',
        created_at=datetime.now()
    )
    car22 = Car(
        owner_id=6,
        make='Bentley',
        model='Continental',
        type='coupe',
        year=2018,
        mileage=29000,
        price=275000,
        color='blue',
        car_description='Blue Bentley Continental',
        created_at=datetime.now()
    )

    all_cars = [car1, car2, car3, car4, car5, car6, car7,
                car8, car9, car10, car11, car12, car13, car14, car15,
                car16, car17, car18, car19, car20, car21, car22]
    add_cars = [db.session.add(car) for car in all_cars]
    db.session.commit()
    print('all cars added')


def undo_cars():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.cars RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM cars"))

    db.session.commit()
