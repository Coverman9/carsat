import "./Modals.css";
import { useModal } from "../../context/Modal";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { deleteReviewThunk } from "../../store/reviews";

const DeleteReviewModal = ({ review }) => {
  const { closeModal } = useModal();
  const dispatch = useDispatch();
  const history = useHistory();

  const confirmDelete = async () => {
    await dispatch(deleteReviewThunk(review.id));
    closeModal();
  };
  return (
    <>
      <div className="delete-modal">
        <h2>Delete Review</h2>
        <p>Are u sure you want remove your review?</p>
        <button className="yes-delete" onClick={confirmDelete}>
          Yes
        </button>
        <button className="no-delete" onClick={closeModal}>
          No
        </button>
      </div>
    </>
  );
};

export default DeleteReviewModal;
