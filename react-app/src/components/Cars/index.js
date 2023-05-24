import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllCarsThunk } from "../../store/cars";
import "./Cars.css";
import { Link } from "react-router-dom";

const getCars = (cars) => {
  let carsObj = cars.reduce((acc, car) => {
    if (acc[car.type]) {
      acc[car.type] = [...acc[car.type], car];
    } else {
      acc[car.type] = [car];
    }
    return acc;
  }, {});
  return carsObj;
};

const Cars = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const carsObj = useSelector((state) => state.cars);
  const carsArr = Object.values(carsObj);
  const cars = getCars(carsArr);
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getAllCarsThunk());
  }, [dispatch]);

  return (
    <>
      <h1 className="all-cars-h1">All Cars</h1>
      <div className="search-car-input">
        <input
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Search for Car"
        />
      </div>
      {Object.keys(cars).map((type) => {

        return (
          <>
            <h3>{type ? type.toUpperCase() : "OTHERS"}</h3>
            <div className="all-cars-container">
              {cars[type]
                .filter(
                  (car) =>
                    car.make.toLowerCase().includes(searchTerm.toLowerCase()) ||
                    car.model.toLowerCase().includes(searchTerm.toLowerCase())
                )
                .map((car) => {
                  return (
                    <>
                      <Link to={`/cars/${car.id}`}>
                        <div className="car-image-info-div">
                          <img src={car?.images[0]?.image} />
                          <div className="all-cars-make-model">
                            <p>
                              {car.make} {car.model}
                            </p>
                            <p className="car-price">${car.price}</p>
                          </div>
                        </div>
                      </Link>
                    </>
                  );
                })}
            </div>
          </>
        );
      })}
    </>
  );
};

export default Cars;
