import { useDispatch, useSelector } from "react-redux";

const Profile = () => {
  const carsObj = useSelector((state) => state.session.user.cars);
  const carsArr = Object.values(carsObj);
  console.log(carsArr);

  return (
    <>
      <h1>Your Profile</h1>
      <div>
        <h2>Your Cars</h2>
        {carsArr.map(car => {
            return (
                <>
                <p>{car.make}</p>
                </>
            )
        })}
      </div>
    </>
  );
};

export default Profile;
