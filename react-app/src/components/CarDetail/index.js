import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getCarDetailThunk } from "../../store/cars";
import { useParams } from "react-router-dom";
import { createReviewThunk, getAllCarReviewsThunk } from "../../store/reviews";
import OpenModalButton from "../OpenModalButton";
import AddReviewModal from "../Modals/AddReviewModal";
import {
  createWishlistThunk,
  deleteWishlistThunk,
  getAllCarWishlistsThunk,
} from "../../store/wishlists";
import {
  createTestdriveThunk,
  getAllCarTestdrivesThunk,
} from "../../store/testdrives";
import "./CarDetail.css";

const CarDetail = () => {
  const [date, setDate] = useState();
  let year = new Date().getFullYear().toString();
  let month = new Date().getMonth();
  let day = new Date().getDate().toString();
  // console.log(`${year}-0${month}-${day}`);
  const { carId } = useParams();
  const sessionUser = useSelector((state) => state.session.user);
  const car = useSelector((state) => state.cars[carId]);
  const reviews = useSelector((state) => state.reviews);
  const reviewsArr = Object.values(reviews);
  const wishlists = useSelector((state) => state.wishlists);
  const wishlistsArr = Object.values(wishlists);
  const testdrives = useSelector((state) => state.testdrives);
  const testdrivesArr = Object.values(testdrives);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getCarDetailThunk(carId));
    dispatch(getAllCarReviewsThunk(carId));
    dispatch(getAllCarWishlistsThunk(carId));
    dispatch(getAllCarTestdrivesThunk(carId));
  }, [dispatch]);

  const addToWishlist = async () => {
    await dispatch(
      createWishlistThunk({
        description: `${sessionUser.firstName} added ${car.make} to his wishlist`,
        carId,
      })
    );
  };

  const removeFromWishlist = async (id) => {
    await dispatch(deleteWishlistThunk(id));
  };

  const formSubmit = async (e) => {
    e.preventDefault();
    await dispatch(
      createTestdriveThunk({
        testdrive_date: date,
        carId,
      })
    );
  };
  const otherImages = car?.images.slice(1)
  console.log(otherImages)
  return (
    <>
      <h1>Car Detail</h1>
      <h2>
        {car?.year} {car?.make} {car?.model}
      </h2>
      <div className="car-detail-image-container">
        <div className="car-detail-main-image">
          <img src={car?.images[0]?.image} />
        </div>
        <div className="car-detail-other-images">
          {otherImages?.map((car) => {
            return (
              <>
                <img src={car.image} />
              </>
            );
          })}
        </div>
      </div>
      <h2>Car Reviews:</h2>
      <div>
        <OpenModalButton
          buttonText={"Add review"}
          modalComponent={<AddReviewModal carId={carId} />}
        />
      </div>
      <div>
        {reviewsArr.map((review) => {
          return (
            <>
              <p>{review.review}</p>
              <p>{review.stars}</p>
            </>
          );
        })}
      </div>
      <div>
        {wishlistsArr.length === 0 ? (
          <div onClick={addToWishlist}>♡</div>
        ) : wishlistsArr.length &&
          wishlistsArr.find(
            (wishlist) => wishlist.userId === sessionUser.id
          ) ? (
          <div
            onClick={() =>
              removeFromWishlist(
                wishlistsArr.find(
                  (wishlist) => wishlist.userId === sessionUser.id
                ).id
              )
            }
          >
            ♥
          </div>
        ) : (
          <div onClick={addToWishlist}>♡</div>
        )}
      </div>
      <p>Count: {wishlistsArr.length}</p>

      <div>
        <label>
          Choose your preferred testdrive date:
          <input
            type="date"
            name="testdrive"
            min={`${year}-0${(month + 1).toString()}-${day}`}
            max="2024-04-20"
            onChange={(e) => setDate(e.target.value)}
            required
          />
          <span class="validity"></span>
        </label>

        <p>
          <button onClick={formSubmit}>Submit</button>
        </p>
      </div>

      <div>
        {testdrivesArr.map((testdrive) => {
          return (
            <>
              <p>
                {testdrive.user.firstName} {testdrive.user.lastName} has
                testdrive in {testdrive.testdrive_date}
              </p>
            </>
          );
        })}
      </div>
    </>
  );
};

export default CarDetail;
