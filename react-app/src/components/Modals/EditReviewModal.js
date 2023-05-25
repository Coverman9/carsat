import { useDispatch } from "react-redux";
import "./Modals.css";
import { useState } from "react";
import { useModal } from "../../context/Modal";
import { updateReviewThunk } from "../../store/reviews";

const EditReviewModal = ({ _review }) => {
    console.log(_review)
  const [review, setReview] = useState(_review.review);
  const [stars, setStars] = useState(_review.stars);
  const [errors, setErrors] = useState([]);

  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const handleSubmit = async (e) => {
    e.preventDefault();
    await dispatch(
      updateReviewThunk({
        review,
        stars,
        reviewId: _review.id
      })
    ).then(() => closeModal());
  };

  return (
    <>
      <div className="edit-review-modal">
        <form onSubmit={handleSubmit}>
          <div className="create-review-modal">
            <h2>Update Review</h2>
            <div>
              <ul>
                {errors.map((error, idx) => (
                  <li className="form-errors" key={idx}>
                    {error}
                  </li>
                ))}
              </ul>
            </div>
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

export default EditReviewModal;
