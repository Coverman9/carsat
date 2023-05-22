# from app.models import db, Image, environment, SCHEMA
# from sqlalchemy.sql import text


# def seed_images():
#     image1 = Image(
#         car_id=1,
#         image='Used to drive this car, its really cool',
#     )
#     image2 = Image(
#         car_id=2,
#         image='Used to drive this car, its really cool',
#     )
#     image3 = Image(
#         car_id=3,
#         image='Used to drive this car, its really cool',
#     )
#     image4 = Image(
#         car_id=4,
#         image='Used to drive this car, its really cool',
#     )
#     image5 = Image(
#         car_id=5,
#         image='Used to drive this car, its really cool',
#     )
#     image6 = Image(
#         car_id=6,
#         image='Used to drive this car, its really cool',
#     )
#     image7 = Image(
#         car_id=7,
#         image='Used to drive this car, its really cool',
#     )
#     image8 = Image(
#         car_id=8,
#         image='Used to drive this car, its really cool',
#     )
#     image9 = Image(
#         car_id=9,
#         image='Used to drive this car, its really cool',
#     )
#     image10 = Image(
#         car_id=10,
#         image='Used to drive this car, its really cool',
#     )
#     image11 = Image(
#         car_id=11,
#         image='Used to drive this car, its really cool',
#     )
#     image12 = Image(
#         car_id=12,
#         image='Used to drive this car, its really cool',
#     )
#     image13 = Image(
#         car_id=13,
#         image='Used to drive this car, its really cool',
#     )
#     image14 = Image(
#         car_id=14,
#         image='Used to drive this car, its really cool',
#     )
#     image15 = Image(
#         car_id=15,
#         image='Used to drive this car, its really cool',
#     )
#     image16 = Image(
#         car_id=16,
#         image='Used to drive this car, its really cool',
#     )
#     image17 = Image(
#         car_id=17,
#         image='Used to drive this car, its really cool',
#     )
#     image18 = Image(
#         car_id=18,
#         image='Used to drive this car, its really cool',
#     )
#     image19 = Image(
#         car_id=19,
#         image='Used to drive this car, its really cool',
#     )
#     image20 = Image(
#         car_id=20,
#         image='Used to drive this car, its really cool',
#     )
#     image21 = Image(
#         car_id=21,
#         image='Used to drive this car, its really cool',
#     )
#     image22 = Image(
#         car_id=22,
#         image='Used to drive this car, its really cool',
#     )

#     all_images = [image1, image2, image3, image4, image5, image6,
#                    image7, image8, image9, image10, image11, image12,
#                    image13, image14, image15, image16, image17, image18,
#                    image19, image20, image21, image22]
#     add_images = [db.session.add(image) for image in all_images]
#     db.session.commit()
#     print('all images added')


# def undo_reviews():
#     if environment == "production":
#         db.session.execute(
#             f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
#     else:
#         db.session.execute(text("DELETE FROM images"))

#     db.session.commit()
