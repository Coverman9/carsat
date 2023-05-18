import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getCarDetailThunk } from "../../store/cars";
import { useParams } from "react-router-dom";

const CarDetail = () => {
  const { carId } = useParams();
  const car = useSelector((state) => state.cars[carId]);
  console.log("SGEIN", car)

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getCarDetailThunk(carId));
  }, [dispatch]);


  return (
    <>
      <h1>Car Detail</h1>
      <h2>{car?.year} {car?.make} {car?.model}</h2>
    </>
  );
};

export default CarDetail;
