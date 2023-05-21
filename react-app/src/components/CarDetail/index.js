import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getCarDetailThunk } from "../../store/cars";
import { useParams } from "react-router-dom";
import { createReviewThunk, getAllCarReviewsThunk } from "../../store/reviews";
import OpenModalButton from "../OpenModalButton";
import AddReviewModal from "../Modals/AddReviewModal";

const CarDetail = () => {
  const { carId } = useParams();
  const car = useSelector((state) => state.cars[carId]);
  const reviews = useSelector((state) => state.reviews)
  const reviewsArr = Object.values(reviews)

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getCarDetailThunk(carId));
  }, [dispatch]);

  useEffect(() => {
    dispatch(getAllCarReviewsThunk(carId))
  }, [dispatch])

  return (
    <>
      <h1>Car Detail</h1>
      <h2>{car?.year} {car?.make} {car?.model}</h2>
      <h2>Car Reviews:</h2>
      <div>
        <OpenModalButton
          buttonText={"Add review"}
          modalComponent={<AddReviewModal carId={carId}/>}
        />
      </div>
      <div>{reviewsArr.map(review => {
        return (
          <>
          <p>{review.review}</p>
          <p>{review.stars}</p>
          </>
        )
      })}</div>

    </>
  );
};

export default CarDetail;
