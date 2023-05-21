import { useDispatch, useSelector } from "react-redux";
import OpenModalButton from "../OpenModalButton";
import EditCarModal from "../Modals/EditCarModal";
import DeleteCarModal from "../Modals/DeleteCarModal";
import EditReviewModal from "../Modals/EditReviewModal";
import DeleteReviewModal from "../Modals/DeleteReviewModal";
import { useEffect } from "react";
import { getAllCarsThunk } from "../../store/cars";
import { getAllUserReviewsThunk } from "../../store/reviews";
import { getAllUserWishlistsThunk } from "../../store/wishlists";

const Profile = () => {
  const sessionUser = useSelector((state) => state.session.user);
  const cars = useSelector(state => state.cars)
  const carsArr = Object.values(cars)
  const userCars = carsArr.filter(el => el.ownerId === sessionUser.id)

  const reviews = useSelector(state => state.reviews)
  const userReviews = Object.values(reviews)

  const wishlists = useSelector(state => state.wishlists)
  const userWishlists = Object.values(wishlists)

  const userTestDrives = Object.values(sessionUser.testDrives)

  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getAllCarsThunk());
    dispatch(getAllUserReviewsThunk(sessionUser.id))
    dispatch(getAllUserWishlistsThunk(sessionUser.id))
  }, [dispatch]);

  useEffect(() => {
  }, [dispatch])

  return (
    <>
      <h1>Profile Page</h1>
      <div>
        <h2>Your Cars</h2>
        {userCars.map((car) => {
          return (
            <>
              <p>
                {car.make} {car.model}
              </p>
              <OpenModalButton
                buttonText={"Update"}
                modalComponent={<EditCarModal car={car} />}
              />
              <OpenModalButton
                buttonText={"Delete"}
                modalComponent={<DeleteCarModal car={car} />}
              />
            </>
          );
        })}
      </div>
      <div>
        <h2>Your Reviews</h2>
        {userReviews.map((review) => {
          return (
            <>
              <p>
                {review.review}
              </p>
              <OpenModalButton
                buttonText={"Update"}
                modalComponent={<EditReviewModal _review={review}/>}
              />
              <OpenModalButton
                buttonText={"Delete"}
                modalComponent={<DeleteReviewModal review={review}/>}
              />
            </>
          );
        })}
      </div>
      <div>
        <h2>Your Wishlist</h2>
        {userWishlists.map((wishlist) => {
          return (
            <>
              <p>
                {wishlist.car.make} {wishlist.car.model}
              </p>
              <OpenModalButton
                buttonText={"Remove"}
                modalComponent={<DeleteCarModal />}
              />
            </>
          );
        })}
      </div>
      <div>
        <h2>Your Testdrive</h2>
        {userTestDrives.map((testdrive) => {
          return (
            <>
              <p>
                {testdrive.startDate} - {testdrive.endDate}
              </p>
              <OpenModalButton
                buttonText={"Update"}
                modalComponent={<EditCarModal />}
              />
              <OpenModalButton
                buttonText={"Delete"}
                modalComponent={<DeleteCarModal />}
              />
            </>
          );
        })}
      </div>
    </>
  );
};

export default Profile;
