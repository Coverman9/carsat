import "./Modals.css";
import { useModal } from "../../context/Modal";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { deleteCarThunk } from "../../store/cars";

const DeleteCarModal = ({ car }) => {
  const { closeModal } = useModal();
  const dispatch = useDispatch();
  const history = useHistory();

  const confirmDelete = async () => {
    await dispatch(deleteCarThunk(car.id));
    closeModal();
  };
  return (
    <>
      <div className="delete-modal">
        <h2>Delete Car</h2>
        <p>Are u sure you want remove your car?</p>
        <button className="yes-delete" onClick={confirmDelete}>Yes</button>
        <button className="no-delete" onClick={closeModal}>No</button>
      </div>
    </>
  );
};

export default DeleteCarModal;
