const ALL_CARS = "cars/ALL_CARS";
const ONE_CAR = "cars/ONE_CAR";
const CREATE_CAR = "cars/CREATE_CAR";
const UPDATE_CAR = "cars/UPDATE_CAR";
const DELETE_CAR = "cars/DELETE_CAR";

const allCarsAction = (cars) => ({
  type: ALL_CARS,
  cars,
});

const oneCarAction = (car) => ({
  type: ONE_CAR,
  car,
});

const createCarAction = (car) => ({
  type: CREATE_CAR,
  car,
});

const updateCarAction = (carId) => ({
  type: UPDATE_CAR,
  carId,
});

const deleteCarAction = (carId) => ({
  type: DELETE_CAR,
  carId,
});

///-------------------THUNK-------------------------

export const getAllCarsThunk = () => async (dispatch) => {
  const res = await fetch("/api/cars");
  const cars = await res.json();

  await dispatch(allCarsAction(cars));
};

///------------------REDUCERS--------------------------

const initialState = {};

const cars = (state = initialState, action) => {
  let newState = {};
  switch (action.type) {
    case ALL_CARS:
      action.cars.cars.forEach((car) => newState[car.id] = car);
      return newState;
    default:
      return state;
  }
}


export default cars
