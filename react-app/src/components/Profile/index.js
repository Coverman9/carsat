import { useDispatch, useSelector } from "react-redux";
import OpenModalButton from "../OpenModalButton";
import EditCarModal from "../Modals/EditCarModal";
import DeleteCarModal from "../Modals/DeleteCarModal";
import EditReviewModal from "../Modals/EditReviewModal";
import DeleteReviewModal from "../Modals/DeleteReviewModal";
import { useEffect } from "react";
import { carImagesThunk, getAllCarsThunk } from "../../store/cars";
import { getAllUserReviewsThunk } from "../../store/reviews";
import { getAllUserWishlistsThunk } from "../../store/wishlists";
import RemoveWishModal from "../Modals/RemoveWishModal";
import { getAllUserTestdrivesThunk } from "../../store/testdrives";
import EditTestdriveModal from "../Modals/EditTestdriveModal";
import CancelTestdriveModal from "../Modals/CancelTestDriveModal";
import AddImageModal from "../Modals/AddImageModal";
import "./Profile.css";
import { Link } from "react-router-dom";

const Profile = () => {
  const sessionUser = useSelector((state) => state.session.user);
  const cars = useSelector((state) => state.cars);
  const carsArr = Object.values(cars);
  const userCars = carsArr.filter((el) => el.ownerId === sessionUser.id);

  const reviews = useSelector((state) => state.reviews);
  const userReviews = Object.values(reviews);

  const wishlists = useSelector((state) => state.wishlists);
  const userWishlists = Object.values(wishlists);

  const testdrives = useSelector((state) => state.testdrives);
  const userTestDrives = Object.values(testdrives);


  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getAllCarsThunk());
    dispatch(getAllUserReviewsThunk(sessionUser.id));
    dispatch(getAllUserWishlistsThunk(sessionUser.id));
    dispatch(getAllUserTestdrivesThunk(sessionUser.id));
    dispatch(carImagesThunk());
  }, [dispatch]);

  useEffect(() => {}, [dispatch]);

  return (
    <>
      <h1>Profile Page</h1>
      <div className="profile-page-main-div">
        <div>
          <h2 className="your-cars-h2">Your Cars</h2>
          {userCars.map((car) => {
            return (
              <>
                <div className="profile-your-cars">
                  <p className="profile-page-cars-make">
                    {car.make} {car.model}
                  </p>
                  <Link to={`/cars/${car.id}`}>
                    <img src={car?.images?.[0]?.image} />
                  </Link>
                  <div>
                    <OpenModalButton
                      buttonText={"Add image"}
                      modalComponent={<AddImageModal car={car} />}
                    />
                    <OpenModalButton
                      buttonText={"Update"}
                      modalComponent={<EditCarModal car={car} />}
                    />
                    <OpenModalButton
                      buttonText={"Delete"}
                      modalComponent={<DeleteCarModal car={car} />}
                    />
                  </div>
                </div>
              </>
            );
          })}
        </div>
        <div>
          <h2>Your Reviews</h2>
          {userReviews.map((review) => {
            return (
              <>
                <div className="car-detail-your-reviews">
                  <p>
                    For: {review.car.make} {review.car.model}
                  </p>
                  <p>Review: {review.review}</p>
                  <p>★ {review.stars}</p>
                  <OpenModalButton
                    buttonText={"Update"}
                    modalComponent={<EditReviewModal _review={review} />}
                  />
                  <OpenModalButton
                    buttonText={"Delete"}
                    modalComponent={<DeleteReviewModal review={review} />}
                  />
                </div>
              </>
            );
          })}
        </div>
        <div>
          <h2 className="your-wishlist-h2">Your Wishlist</h2>
          {userWishlists.map((wishlist) => {
            return (
              <>
                <div className="profile-wishlist-div">
                  <p>
                    {wishlist.car.year} {wishlist.car.make} {wishlist.car.model}
                  </p>
                  <OpenModalButton
                    buttonText={"Remove"}
                    modalComponent={<RemoveWishModal wishlist={wishlist} />}
                  />
                </div>
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
                  {testdrive.testdrive_date} - {testdrive.car.carDescription}
                </p>
                <OpenModalButton
                  buttonText={"Update"}
                  modalComponent={<EditTestdriveModal testdrive={testdrive} />}
                />
                <OpenModalButton
                  buttonText={"Cancel"}
                  modalComponent={
                    <CancelTestdriveModal testdrive={testdrive} />
                  }
                />
              </>
            );
          })}
        </div>
      </div>
    </>
  );
};

export default Profile;
