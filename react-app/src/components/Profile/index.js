import { useDispatch, useSelector } from "react-redux";
import OpenModalButton from "../OpenModalButton";
import EditCarModal from "../Modals/EditCarModal";
import DeleteCarModal from "../Modals/DeleteCarModal";
import { useEffect } from "react";
import { getAllCarsThunk } from "../../store/cars";

const Profile = () => {
  const test = useSelector(state => state.cars)
  const sessionUser = useSelector((state) => state.session.user);
  const testArr = Object.values(test)
  const userCars = testArr.filter(el => el.ownerId === sessionUser.id)
  const userReviews = Object.values(sessionUser.reviews)
  const userWishlists = Object.values(sessionUser.wishlists)
  const userTestDrives = Object.values(sessionUser.testDrives)

  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getAllCarsThunk());
  }, [dispatch]);

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
