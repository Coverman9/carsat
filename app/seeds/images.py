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
    car2_image1 = Image(
        car_id=2,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/006f9be719e242cb996d4b923421675f.jpeg'
    )
    car2_image2 = Image(
        car_id=2,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/3a0ca6a751f948faacd16782dcc5fcaa.jpeg'
    )
    car2_image3 = Image(
        car_id=2,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/38eb2b3ecfe8492eb29e9a36337b7e38.jpeg'
    )
    car2_image4 = Image(
        car_id=2,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/15c838f6a54e4cd988d93148370ff566.jpeg'
    )
    car3_image1 = Image(
        car_id=3,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/bf1b3bdaa7f645f1a80f0ca56ab9b55d.jpeg'
    )
    car3_image2 = Image(
        car_id=3,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/6b4481b4a31e4885800e9e504c573a67.jpeg'
    )
    car3_image3 = Image(
        car_id=3,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/bb2cb6361f484ba8b722f465d723d1d0.jpeg'
    )
    car3_image4 = Image(
        car_id=3,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/7de3517a072c4b90991785c343ec44c8.jpeg'
    )
    car4_image1 = Image(
        car_id=4,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/296889e844cd4c5bb0d246829529373f.jpeg'
    )
    car4_image2 = Image(
        car_id=4,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/a8fe69c72cda48578083ca6e93419394.jpeg'
    )
    car4_image3 = Image(
        car_id=4,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/8a164edc6a0e4004ba53e61b68b6424b.jpeg'
    )
    car4_image4 = Image(
        car_id=4,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/bf367eca93794e25b7d93a24457c4140.jpeg'
    )
    car5_image1 = Image(
        car_id=5,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/f246b0619f5d484ca6509685d1ee0002.jpeg'
    )
    car5_image2 = Image(
        car_id=5,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/b8c08b806c0040e2b463098103a64fbc.jpeg'
    )
    car5_image3 = Image(
        car_id=5,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/b54df14f60814c5d856cd19cf44525f5.jpeg'
    )
    car5_image4 = Image(
        car_id=5,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/6c3c6f90495940e18b9cb5dd2fedaa6d.jpeg'
    )
    car6_image1 = Image(
        car_id=6,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/cb70302968ee420399626bb162b14bc5.jpeg'
    )
    car6_image2 = Image(
        car_id=6,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/dc1af9174ee7402cb5f260f539bd57ba.jpeg'
    )
    car6_image3 = Image(
        car_id=6,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/d2e8d4124eb149f3a97a1f29828b663b.jpeg'
    )
    car6_image4 = Image(
        car_id=6,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/849d8bb4061c43e5b052f40d93534bec.jpeg'
    )
    car7_image1 = Image(
        car_id=7,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/31440131abb142db86c10e92eb8acc43.jpeg'
    )
    car7_image2 = Image(
        car_id=7,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/e59bce1941b84224a7ba8d4ce9bd9398.jpeg'
    )
    car7_image3 = Image(
        car_id=7,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/c1e054c9570e4df9b6a37d0e4c123f16.jpeg'
    )
    car7_image4 = Image(
        car_id=7,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/cf93171c10a64c678ac073ddda1419aa.jpeg'
    )
    car8_image1 = Image(
        car_id=8,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/d4ebd52c5db64d5991a0c93f8fa5c277.jpeg'
    )
    car8_image2 = Image(
        car_id=8,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/a2e9f6ecb78143dda12ee2d50b43cd09.jpeg'
    )
    car8_image3 = Image(
        car_id=8,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/ee4942f196dd45d7b555ef2f4de1add1.jpeg'
    )
    car8_image4 = Image(
        car_id=8,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/578d58c5b91d47fc92ace7a17e853922.jpeg'
    )
    car9_image1 = Image(
        car_id=9,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/b496fd1d5b894e52b260b5c0b4c2b533.jpeg'
    )
    car9_image2 = Image(
        car_id=9,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/b0a464d719f04615a4ce4d79b91ece51.jpeg'
    )
    car9_image3 = Image(
        car_id=9,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/36a38fa386054f98bba714447f0360e5.jpeg'
    )
    car9_image4 = Image(
        car_id=9,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/096187515c9541519c3ae6554398d662.jpeg'
    )
    car10_image1 = Image(
        car_id=10,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/45015f5eac514188b6f25afadc927541.jpeg'
    )
    car10_image2 = Image(
        car_id=10,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/761c0b66cca3492195db81665aeccd25.jpeg'
    )
    car10_image3 = Image(
        car_id=10,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/a7e3f46244e447eb8783c9262a874440.jpeg'
    )
    car10_image4 = Image(
        car_id=10,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/46b60c0b8feb4078a54672e1df5f0dcc.jpeg'
    )
    car11_image1 = Image(
        car_id=11,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/6abdbf798ac340199d64fe6b5eeeda2c.jpeg'
    )
    car11_image2 = Image(
        car_id=11,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/74ca731dc7434957a77eb0af533500d3.jpeg'
    )
    car11_image3 = Image(
        car_id=11,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/e5c9f2e374e7461eb58889377e972f7d.jpeg'
    )
    car11_image4 = Image(
        car_id=11,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/73c4377870494d13b047d0be40596404.jpeg'
    )
    car12_image1 = Image(
        car_id=12,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/207523818446494d8687c7ce00ea07a3.jpeg'
    )
    car12_image2 = Image(
        car_id=12,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/a733927ad9c74c0c8d602fbf00b5df4f.jpeg'
    )
    car12_image3 = Image(
        car_id=12,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/de3fc29098e54f6db7ad3064c9bba94a.jpeg'
    )
    car12_image4 = Image(
        car_id=12,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/93cf6df194854e2c916ce8f281979c6a.jpeg'
    )
    car13_image1 = Image(
        car_id=13,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/7bf813f6250d4f86b74dd9927bcf96bd.jpeg'
    )
    car13_image2 = Image(
        car_id=13,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/5f5fe19cc6a04293adedd05b88b1962e.jpeg'
    )
    car13_image3 = Image(
        car_id=13,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/1dbaf64de08a4c4ab6ccf083daf6f716.jpeg'
    )
    car13_image4 = Image(
        car_id=13,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/c9d2ef2f6ab44a59981936fb2be6856d.jpeg'
    )
    car14_image1 = Image(
        car_id=14,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/22754d0f64a6442ea16f74ce5d1e55ab.jpeg'
    )
    car14_image2 = Image(
        car_id=14,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/54368b4c4da541808d8c5accc220831a.jpeg'
    )
    car14_image3 = Image(
        car_id=14,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/dc0583877bf14afbb8c218c01a5e0b24.jpeg'
    )
    car14_image4 = Image(
        car_id=14,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/3ffe385587784ea684f590b43c1c5dbc.jpeg'
    )
    car15_image1 = Image(
        car_id=15,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/c3fc6d0c293b4a2d9b465a40316e662e.jpeg'
    )
    car15_image2 = Image(
        car_id=15,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/24fa6a20ea624997a68598bb2b1bc138.jpeg'
    )
    car15_image3 = Image(
        car_id=15,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/58d0cd9d574d4dce962b6a6929d823bf.jpeg'
    )
    car15_image4 = Image(
        car_id=15,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/114a818d84f44638b6d6f1340c0cbfda.jpeg'
    )
    car16_image1 = Image(
        car_id=16,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/e07f3ba2b49e47c69ab8492af07ec603.jpeg'
    )
    car16_image2 = Image(
        car_id=16,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/73c876fd33a1486ba72706d4df2ba3ad.jpeg'
    )
    car16_image3 = Image(
        car_id=16,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/29ca17e3a50c440485530e7b27da8e91.jpeg'
    )
    car16_image4 = Image(
        car_id=16,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/b3465035ba4f4839a283abc2197d5324.jpeg'
    )
    car17_image1 = Image(
        car_id=17,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/fdb2f3749bbf46e69584abc8e929fcd1.jpeg'
    )
    car17_image2 = Image(
        car_id=17,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/76d4d1d8b82e41288ca4215c72edc6a9.jpeg'
    )
    car17_image3 = Image(
        car_id=17,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/3b9857aafeb1427eb7f7cd0c74824d78.jpeg'
    )
    car17_image4 = Image(
        car_id=17,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/4c9591043f7f4bc98068c7a5ebcfd52b.jpeg'
    )
    car18_image1 = Image(
        car_id=18,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/ed881066a4aa4734b8e8bdab4608cf00.jpeg'
    )
    car18_image2 = Image(
        car_id=18,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/c673890fe3cc40b081d8198ddc9cf96b.jpeg'
    )
    car18_image3 = Image(
        car_id=18,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/c3cdb662997640a8a1ccb3b432399c45.jpeg'
    )
    car18_image4 = Image(
        car_id=18,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/0a2a12656394441a8978347756227e5a.jpeg'
    )
    car21_image1 = Image(
        car_id=21,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/585a5746a9534d1c9a89e19b6c12fa21.jpeg'
    )
    car21_image2 = Image(
        car_id=21,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/c83122249c77465a9480223cec17c36f.jpeg'
    )
    car21_image3 = Image(
        car_id=21,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/f57815cc45624b8599f1d562784f0338.jpeg'
    )
    car21_image4 = Image(
        car_id=21,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/578b7d65e869429a96306558743b5818.jpeg'
    )
    car22_image1 = Image(
        car_id=22,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/94d7cf38e04c4c038f013cf911e6cb0e.jpeg'
    )
    car22_image2 = Image(
        car_id=22,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/352fe256ae0742b78ff154f9601cf119.jpeg'
    )
    car22_image3 = Image(
        car_id=22,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/886baf6f976348b69ada4b0ac5b68a27.jpeg'
    )
    car22_image4 = Image(
        car_id=22,
        image='https://carsat-aws.s3.us-east-2.amazonaws.com/dcfdee0194d94a55837d84c309f6efba.jpeg'
    )

    all_images = [image1, image2, image3, image4, image5, image6,
                   image7, image8, image9, image10, image11, image12,
                   image13, image14, image15, image16, image17, image18,
                   image19, image20, image21, image22, car1_image1, car1_image2,
                   car1_image3,car1_image4,car2_image1,car2_image2,car2_image3,
                   car2_image4,car3_image1,car3_image2,car3_image3,car3_image4,car4_image1,
                   car4_image2,car4_image3,car4_image4,car5_image1,car5_image2,car5_image3,
                   car5_image4,car6_image1,car6_image2,car6_image3,car6_image4,car7_image1,
                   car7_image2,car7_image3,car7_image4,car8_image1,car8_image2,car8_image3,
                   car8_image4,car9_image1,car9_image2,car9_image3,car9_image4,car10_image1,
                   car10_image2,car10_image3,car10_image4,car11_image1,car11_image2,car11_image3,
                   car11_image4,car12_image1,car12_image2,car12_image3,car12_image4,car13_image1,
                   car13_image2,car13_image3,car13_image4,car14_image1,car14_image2,car14_image3,
                   car14_image4,car15_image1,car15_image2,car15_image3,car15_image4,car16_image1,
                   car16_image2,car16_image3,car16_image4,car17_image1,car17_image2,car17_image3,
                   car17_image4,car18_image1,car18_image2,car18_image3,car18_image4,
                   car21_image1,car21_image2,car21_image3,
                   car21_image4,car22_image1,car22_image2,car22_image3,car22_image4]
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
