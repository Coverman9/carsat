import { useEffect } from "react";
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
  const carsObj = useSelector((state) => state.cars);
  const carsArr = Object.values(carsObj);
  const cars = getCars(carsArr);
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getAllCarsThunk());
  }, [dispatch]);

  return (
    <>
      <h1>All Cars</h1>
      {Object.keys(cars).map((type) => {
        return (
          <>
            <h3>{type.toUpperCase()}</h3>
            <div>
              {cars[type].map((car) => {
                return (
                  <>
                    <Link to={`/cars/${car.id}`}>
                      <div>
                        {car.make} {car.model}
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
