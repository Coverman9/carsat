import "./Modals.css";
import { useModal } from "../../context/Modal";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { cancelTestdriveThunk } from "../../store/testdrives";

const CancelTestdriveModal = ({ testdrive }) => {
  const { closeModal } = useModal();
  const dispatch = useDispatch();
  const history = useHistory();

  const confirmCancel = async () => {
    await dispatch(cancelTestdriveThunk(testdrive.id));
    closeModal();
  };
  return (
    <>
      <div className="delete-modal">
        <h2>Cancel Test drive</h2>
        <p>Are you sure you want to cancel testdrive?</p>
        <button className="yes-delete" onClick={confirmCancel}>
          Yes
        </button>
        <button className="no-delete" onClick={closeModal}>
          No
        </button>
      </div>
    </>
  );
};

export default CancelTestdriveModal;
