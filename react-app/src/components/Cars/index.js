import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllCarsThunk } from "../../store/cars";

const Cars = () => {
  const carsObj = useSelector((state) => state.cars);
  const cars = Object.values(carsObj)

  const dispatch = useDispatch()
  useEffect(() => {
    dispatch(getAllCarsThunk())
  }, [dispatch])

  return (
    <>
      <h1>All Cars</h1>
      {cars.map((car) => {
        return (
            <>
            <p>{car.make}</p>
            </>
        )
      })}
    </>
  );
};

export default Cars;
