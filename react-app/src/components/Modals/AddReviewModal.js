import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { createReviewThunk } from "../../store/reviews";
import "./Modals.css";

const AddReviewModal = ({ carId }) => {
  const [review, setReview] = useState("");
  const [stars, setStars] = useState(0);
  const [errors, setErrors] = useState([]);
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  console.log(stars);
  const handleSubmit = async (e) => {
    e.preventDefault();
    await dispatch(
      createReviewThunk({
        review,
        stars,
        carId
      })
    ).then(() => closeModal());
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div className="create-review-modal">
          <h2>Add Review:</h2>
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
          <div>
            <button>Submit</button>
          </div>
        </div>
      </form>
    </>
  );
};

export default AddReviewModal;
