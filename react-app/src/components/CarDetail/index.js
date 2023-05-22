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

const CarDetail = () => {
  const [date, setDate] = useState();

  let year = new Date().getFullYear().toString();
  let month = new Date().getMonth();
  let day = new Date().getDate().toString();
  console.log(`${year}-0${month}-${day}`);
  const { carId } = useParams();
  const sessionUser = useSelector((state) => state.session.user);
  const car = useSelector((state) => state.cars[carId]);
  const reviews = useSelector((state) => state.reviews);
  const reviewsArr = Object.values(reviews);
  const wishlists = useSelector((state) => state.wishlists);
  const wishlistsArr = Object.values(wishlists);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getCarDetailThunk(carId));
    dispatch(getAllCarReviewsThunk(carId));
    dispatch(getAllCarWishlistsThunk(carId));
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
  return (
    <>
      <h1>Car Detail</h1>
      <h2>
        {car?.year} {car?.make} {car?.model}
      </h2>
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
        <form>
          <label>
            Choose your preferred testdrive date:
            <input
              type="date"
              name="testdrive"
              min={`${year}-0${(month + 1).toString()}-${day}`}
              max="2024-04-20"
              required
            />
            <span class="validity"></span>
          </label>

          <p>
            <button>Submit</button>
          </p>
        </form>
      </div>
    </>
  );
};

export default CarDetail;
