from app.models import db, Image, environment, SCHEMA
from sqlalchemy.sql import text


def seed_images():
    image1 = Image(
        car_id=1,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/a8542e70ab444e0c892d1ccc980e9c52.jpeg',
    )
    image2 = Image(
        car_id=2,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/4d1e37d863f0467086285c1b9b64400f.jpeg',
    )
    image3 = Image(
        car_id=3,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/93df09aff31a4417a770a962e39c03f4.jpeg',
    )
    image4 = Image(
        car_id=4,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/1fe0e45f724446dfacce38efba4283fc.jpeg',
    )
    image5 = Image(
        car_id=5,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/e9fdaabd76a44d9fb87329c8b16d96fd.jpeg',
    )
    image6 = Image(
        car_id=6,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/2c0a0287535544b5be508db512f90ed9.jpeg',
    )
    image7 = Image(
        car_id=7,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/f9a6449941e2410396bfffef9228c15d.jpeg',
    )
    image8 = Image(
        car_id=8,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/f63368a543244cfda651e6e2c1543080.jpeg',
    )
    image9 = Image(
        car_id=9,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/175679e0156743f4940b292d0a0fe8ba.jpeg',
    )
    image10 = Image(
        car_id=10,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/987b910c1eaa4a16b8d7d16add5fd2b8.jpeg',
    )
    image11 = Image(
        car_id=11,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/6b5c9fbf23494b05a7aa419c4fd923cb.jpeg',
    )
    image12 = Image(
        car_id=12,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/21113ff1e09042e7b3e2c5879fbe538e.jpeg',
    )
    image13 = Image(
        car_id=13,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/bac49faf1b07472f9db1e32ecbc22bf2.jpeg',
    )
    image14 = Image(
        car_id=14,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/cacad82383384766bd3753bb17174566.jpeg',
    )
    image15 = Image(
        car_id=15,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/30f1fd4a9bda4e2382ab0fdad557032a.jpeg',
    )
    image16 = Image(
        car_id=16,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/f4172ef1883f4198bcb99ce9dfaabe52.jpeg',
    )
    image17 = Image(
        car_id=17,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/b20276753aca41fd9b1a26ec1b15005a.jpeg',
    )
    image18 = Image(
        car_id=18,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/f0216b7410434405baa4a1aed278b4b3.jpeg',
    )
    image19 = Image(
        car_id=19,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/16afd1305481486badc68cbe6ce3b0af.jpeg',
    )
    image20 = Image(
        car_id=20,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/f78b8a0b8bae4d389cd616d608513c95.jpeg',
    )
    image21 = Image(
        car_id=21,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/6cbf472a2ebe48839df25e92e69bd300.jpeg',
    )
    image22 = Image(
        car_id=22,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/d65f4855c80d4bad8156e65cbf17a7fe.jpeg',
    )
    car1_image1 = Image(
        car_id=1,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/d89b480254c4410787bd280606d759f2.jpeg'
    )
    car1_image2 = Image(
        car_id=1,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/9c30e864e2434eec8b9d1a473e58d5ac.jpeg'
    )
    car1_image3 = Image(
        car_id=1,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/368f606ed2a646a094ee6fadcfac9275.jpeg'
    )
    car1_image4 = Image(
        car_id=1,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/155c5801d0b342b1b75f2a85fa3cdf39.jpeg'
    )

    all_images = [image1, image2, image3, image4, image5, image6,
                   image7, image8, image9, image10, image11, image12,
                   image13, image14, image15, image16, image17, image18,
                   image19, image20, image21, image22]
    add_images = [db.session.add(image) for image in all_images]
    db.session.commit()
    print('all images added')


def undo_images():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))

    db.session.commit()
