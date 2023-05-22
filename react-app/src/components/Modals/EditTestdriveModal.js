import { useDispatch } from "react-redux";
import "./Modals.css";
import { useState } from "react";
import { useModal } from "../../context/Modal";
import { updateTestdriveThunk } from "../../store/testdrives";

const EditTestdriveModal = ({ testdrive }) => {
    console.log(testdrive)
  const [date, setDate] = useState(testdrive.testdrive_date);
  let year = new Date().getFullYear().toString();
  let month = new Date().getMonth();
  let day = new Date().getDate().toString();
  const [errors, setErrors] = useState([]);

  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const handleSubmit = async (e) => {
    e.preventDefault();
    await dispatch(
      updateTestdriveThunk({
        testdriveId: testdrive.id,
        testdrive_date: date
      })
    ).then(() => closeModal());
  };

  return (
    <>
         <div>
        <label>
          Choose your new testdrive date:
          <input
            type="date"
            name="testdrive"
            value={date}
            min={`${year}-0${(month + 1).toString()}-${day}`}
            max="2024-04-20"
            onChange={(e) => setDate(e.target.value)}
            required
          />
          <span class="validity"></span>
        </label>

        <p>
          <button onClick={handleSubmit}>Submit</button>
        </p>
      </div>
    </>
  );
};

export default EditTestdriveModal;
