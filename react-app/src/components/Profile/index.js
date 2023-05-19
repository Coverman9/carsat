import { useDispatch, useSelector } from "react-redux";
import OpenModalButton from "../OpenModalButton";
import EditCarModal from "../Modals/EditCarModal";
import DeleteCarModal from "../Modals/DeleteCarModal";
import { useEffect } from "react";
import { getAllCarsThunk } from "../../store/cars";
import { getAllUserReviewsThunk } from "../../store/reviews";

const Profile = () => {
  const sessionUser = useSelector((state) => state.session.user);
  const cars = useSelector(state => state.cars)
  const carsArr = Object.values(cars)
  const userCars = carsArr.filter(el => el.ownerId === sessionUser.id)

  const reviews = useSelector(state => state.reviews)
  const userReviews = Object.values(sessionUser.reviews)
  const userWishlists = Object.values(sessionUser.wishlists)
  const userTestDrives = Object.values(sessionUser.testDrives)

  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getAllCarsThunk());
  }, [dispatch]);

  useEffect(() => {
    dispatch(getAllUserReviewsThunk(sessionUser.id))
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
      <div>
        <h2>Your Wishlist</h2>
        {userWishlists.map((wishlist) => {
          return (
            <>
              <p>
                {wishlist.id}
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
