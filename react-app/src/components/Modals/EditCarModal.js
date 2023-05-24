import { useDispatch } from "react-redux";
import "./Modals.css";
import { useState } from "react";
import { updateCarThunk } from "../../store/cars";
import { useModal } from "../../context/Modal";

const EditCarModal = ({ car }) => {
  const [make, setMake] = useState(car.make);
  const [model, setModel] = useState(car.model);
  const [type, setType] = useState(car.type);
  const [year, setYear] = useState(car.year);
  const [mileage, setMileage] = useState(car.mileage);
  const [price, setPrice] = useState(car.price);
  const [color, setColor] = useState(car.color);
  const [carDescription, setCarDescription] = useState(car.carDescription);
  const [errors, setErrors] = useState([]);

  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const types = ["business", "cabrio", "coupe", "sportcar", "SUV", "van"];
  const handleSubmit = async (e) => {
    e.preventDefault();
    await dispatch(
      updateCarThunk({
        make,
        model,
        type,
        year,
        mileage,
        price,
        color,
        car_description: carDescription,
        carId: car.id,
      })
    ).then(() => closeModal());
  };

  return (
    <>
      <div className="update-info-modal">
        <form onSubmit={handleSubmit}>
          <h2>Update Car</h2>
          <ul>
            {errors.map((error, idx) => (
              <li className="form-errors" key={idx}>
                {error}
              </li>
            ))}
          </ul>
          <div className="car-name-desc">
            <div className="create-car-name">
              <label>
                Make:
                <input
                  className="create-car-inputfeild"
                  type="text"
                  value={make}
                  onChange={(e) => setMake(e.target.value)}
                  required
                  placeholder="Make"
                />
              </label>
            </div>
            <div className="create-car-name">
              <label>
                Model:
                <input
                  className="create-car-inputfeild"
                  type="text"
                  value={model}
                  onChange={(e) => setModel(e.target.value)}
                  required
                  placeholder="Model"
                />
              </label>
            </div>
            <div className="create-car-name">
              <label>Choose Car type:</label>
              <select value={type} onChange={(e) => setType(e.target.value)}>
                {types.map((type) => (
                  <option value={type} key={type}>
                    {type}
                  </option>
                ))}
              </select>
            </div>
            <div className="create-car-name">
              <label>
                Year:
                <input
                  className="create-car-inputfeild"
                  type="number"
                  value={year}
                  onChange={(e) => setYear(e.target.value)}
                  required
                  placeholder="Year"
                />
              </label>
            </div>
            <div className="create-car-name">
              <label>
                Mileage:
                <input
                  className="create-car-inputfeild"
                  type="number"
                  value={mileage}
                  onChange={(e) => setMileage(e.target.value)}
                  placeholder="Mileage"
                />
              </label>
            </div>
            <div className="create-car-name">
              <label>
                Price:
                <input
                  className="create-car-inputfeild"
                  type="number"
                  value={price}
                  onChange={(e) => setPrice(e.target.value)}
                  required
                  placeholder="Price"
                />
              </label>
            </div>
            <div className="create-car-name">
              <label>
                Color:
                <input
                  className="create-car-inputfeild"
                  type="text"
                  value={color}
                  onChange={(e) => setColor(e.target.value)}
                  required
                  placeholder="Color"
                />
              </label>
            </div>
            <div className="create-car-textarea">
              <label>
                <textarea
                  className="create-car-inputfeild"
                  rows="5"
                  cols="40"
                  type="text"
                  value={carDescription}
                  onChange={(e) => setCarDescription(e.target.value)}
                  placeholder="Car description"
                />
              </label>
            </div>
          </div>

          <div className="create-car-submit-div">
            <button className="create-car-submit">Submit</button>
          </div>
        </form>
      </div>
    </>
  );
};

export default EditCarModal;
