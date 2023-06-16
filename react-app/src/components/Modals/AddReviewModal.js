import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { createReviewThunk } from "../../store/reviews";
import "./Modals.css";

const AddReviewModal = ({ carId }) => {
  const [review, setReview] = useState("");
  const [stars, setStars] = useState(0);
  const [errors, setErrors] = useState({});
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  console.log(stars);
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (stars === 0) {
      return setErrors({
        message: "Stars cannot be zero",
      });
    }
    if (review.trim().length === 0) {
      return setErrors({
        message: "Need some review"
      })
    }
    await dispatch(
      createReviewThunk({
        review,
        stars,
        carId,
      })
    ).then(() => closeModal());
  };

  return (
    <>
      <div className="edit-review-modal">
        <form onSubmit={handleSubmit}>
          <div className="create-review-modal">
            <h2>Add Review:</h2>
            <div className="form-errors">{errors && errors.message}</div>
            <div>
              <label>
                <textarea
                  type="text"
                  cols="40"
                  rows="7"
                  value={review}
                  onChange={(e) => setReview(e.target.value)}
                  required
                  placeholder="Review"
                />
              </label>
            </div>
            <div className="star-rating">
              {[...Array(5)].map((rating, index) => {
                index += 1;
                return (
                  <button
                    type="button"
                    key={index}
                    className={index <= stars ? "on" : "off"}
                    onClick={() => setStars(index)}
                  >
                    <span className="star">&#9733;</span>
                  </button>
                );
              })}
            </div>
            <div className="create-car-review-div">
              <button className="create-car-review">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </>
  );
};

export default AddReviewModal;
