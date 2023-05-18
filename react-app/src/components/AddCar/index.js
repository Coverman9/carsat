import { useState } from "react";
import "./AddCar.css";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { CreateCarThunk } from "../../store/cars";

const AddCar = () => {
  const [make, setMake] = useState("");
  const [model, setModel] = useState("");
  const [type, setType] = useState("");
  const [year, setYear] = useState(0);
  const [mileage, setMileage] = useState(0);
  const [price, setPrice] = useState(0);
  const [color, setColor] = useState("");
  const [carDescription, setCarDescription] = useState("");
  const [errors, setErrors] = useState([]);

  const dispatch = useDispatch();
  const history = useHistory();
  const types = ["business", "cabrio", "coupe", "sportcar", "SUV", "van"];

  const handleSubmit = async (e) => {
    e.preventDefault();
    dispatch(
      CreateCarThunk({
        make,
        model,
        type,
        year,
        mileage,
        price,
        color,
        car_description: carDescription,
      })
    )
      .then((newCar) => history.push(`/cars/${newCar.id}`))
      .catch(async (res) => {
        const data = await res.json();
        if (data && data.errors) {
          setErrors(data.errors);
        }
      });
  };
  return (
    <>
      <div>
        <form onSubmit={handleSubmit}>
          <h2>Adding new Car</h2>
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

export default AddCar;
